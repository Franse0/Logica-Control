"""GitHub API integration for ADW workflow."""

import os
import subprocess
import json
import urllib.request
import urllib.error
from typing import Optional, Tuple, Dict, Any
from dotenv import load_dotenv
from data_types import GitHubIssue

load_dotenv()


def get_github_token() -> Optional[str]:
    """Get GitHub token from environment or gh CLI."""
    # Try GITHUB_PAT from .env first
    token = os.getenv("GITHUB_PAT")
    if token and token.strip():
        return token.strip()

    # Fall back to gh CLI auth if available
    try:
        result = subprocess.run(
            ["gh", "auth", "token"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def github_api_request(endpoint: str, method: str = "GET", data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Make a request to GitHub API.

    Args:
        endpoint: API endpoint (e.g., "/repos/owner/repo/issues/1")
        method: HTTP method (GET, POST, PATCH, etc.)
        data: Optional JSON data for POST/PATCH requests

    Returns:
        JSON response as dictionary

    Raises:
        RuntimeError: If request fails
    """
    token = get_github_token()
    if not token:
        raise RuntimeError("GitHub token not found. Set GITHUB_PAT in .env or run 'gh auth login'")

    url = f"https://api.github.com{endpoint}"

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    # Prepare request
    req_data = json.dumps(data).encode('utf-8') if data else None
    request = urllib.request.Request(url, data=req_data, headers=headers, method=method)

    try:
        with urllib.request.urlopen(request) as response:
            return json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8')
        raise RuntimeError(f"GitHub API error ({e.code}): {error_body}")
    except Exception as e:
        raise RuntimeError(f"GitHub API request failed: {str(e)}")


def extract_repo_path(logger=None) -> Tuple[str, str]:
    """Extract GitHub repo owner and name from environment or git remote.

    Returns:
        Tuple of (owner, repo_name)
    """
    # Try environment variables first
    owner = os.getenv("GITHUB_REPO_OWNER")
    repo_name = os.getenv("GITHUB_REPO_NAME")

    if owner and repo_name:
        return owner, repo_name

    # Fall back to git remote
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            capture_output=True,
            text=True,
            check=True
        )
        remote_url = result.stdout.strip()

        # Parse URL: https://github.com/owner/repo.git or git@github.com:owner/repo.git
        if "github.com" in remote_url:
            # Remove .git suffix
            if remote_url.endswith(".git"):
                remote_url = remote_url[:-4]

            # Extract owner/repo
            if remote_url.startswith("https://"):
                parts = remote_url.split("github.com/")[1].split("/")
            elif remote_url.startswith("git@"):
                parts = remote_url.split("github.com:")[1].split("/")
            else:
                raise ValueError(f"Unknown git remote format: {remote_url}")

            return parts[0], parts[1]
    except Exception as e:
        if logger:
            logger.error(f"Failed to extract repo path: {e}")
        raise ValueError(f"Could not determine GitHub repo. Set GITHUB_REPO_OWNER and GITHUB_REPO_NAME in .env")


def get_repo_url() -> str:
    """Get the GitHub repository URL."""
    owner, repo_name = extract_repo_path()
    return f"https://github.com/{owner}/{repo_name}"


def fetch_issue(issue_number: str, repo_path: Optional[Tuple[str, str]] = None) -> GitHubIssue:
    """Fetch GitHub issue details using GitHub API.

    Args:
        issue_number: Issue number to fetch
        repo_path: Optional tuple of (owner, repo_name). If not provided, extracted from environment.

    Returns:
        GitHubIssue object
    """
    if repo_path is None:
        repo_path = extract_repo_path()

    owner, repo_name = repo_path
    endpoint = f"/repos/{owner}/{repo_name}/issues/{issue_number}"

    issue_data = github_api_request(endpoint)

    # Convert API response to GitHubIssue format
    return GitHubIssue(
        number=issue_data["number"],
        title=issue_data["title"],
        body=issue_data.get("body"),
        state=issue_data["state"],
        html_url=issue_data["html_url"],
        user=issue_data["user"],
        labels=issue_data.get("labels", []),
        created_at=issue_data["created_at"],
        updated_at=issue_data["updated_at"]
    )


def make_issue_comment(issue_number: int, comment: str, repo_path: Optional[Tuple[str, str]] = None) -> bool:
    """Post a comment on a GitHub issue using GitHub API.

    Args:
        issue_number: Issue number
        comment: Comment text
        repo_path: Optional tuple of (owner, repo_name)

    Returns:
        True if successful, False otherwise
    """
    if repo_path is None:
        repo_path = extract_repo_path()

    owner, repo_name = repo_path
    endpoint = f"/repos/{owner}/{repo_name}/issues/{issue_number}/comments"

    try:
        github_api_request(endpoint, method="POST", data={"body": comment})
        return True
    except RuntimeError as e:
        print(f"Failed to comment on issue #{issue_number}: {e}")
        return False


def mark_issue_in_progress(issue_number: int, repo_path: Optional[Tuple[str, str]] = None) -> bool:
    """Mark an issue as in progress by adding a label.

    Args:
        issue_number: Issue number
        repo_path: Optional tuple of (owner, repo_name)

    Returns:
        True if successful, False otherwise
    """
    if repo_path is None:
        repo_path = extract_repo_path()

    owner, repo_name = repo_path
    endpoint = f"/repos/{owner}/{repo_name}/issues/{issue_number}/labels"

    try:
        github_api_request(endpoint, method="POST", data={"labels": ["in-progress"]})
        return True
    except RuntimeError as e:
        print(f"Failed to mark issue #{issue_number} as in progress: {e}")
        return False
