#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test GitHub integration."""

import sys
import os

# Add parent directory to path to import modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from github import get_github_token, extract_repo_path, fetch_issue
from dotenv import load_dotenv

load_dotenv()


def test_github_integration():
    """Test GitHub API integration."""
    print("=" * 60)
    print("Testing GitHub Integration")
    print("=" * 60)
    print()

    # Test 1: Check GitHub token
    print("1. Checking GitHub token...")
    token = get_github_token()
    if token:
        print(f"   [OK] Token found: {token[:7]}...{token[-4:]}")
    else:
        print("   [ERROR] No GitHub token found!")
        print("   -> Set GITHUB_PAT in .env")
        return False
    print()

    # Test 2: Check repo configuration
    print("2. Checking repo configuration...")
    try:
        owner, repo_name = extract_repo_path()
        print(f"   [OK] Repo: {owner}/{repo_name}")
    except ValueError as e:
        print(f"   [ERROR] {e}")
        return False
    print()

    # Test 3: Try to fetch an issue (if exists)
    print("3. Testing API connection...")
    print("   Enter an issue number to test (or press Enter to skip):")
    issue_num = input("   Issue #: ").strip()

    if issue_num:
        try:
            issue = fetch_issue(issue_num)
            print(f"   [OK] Successfully fetched issue #{issue.number}")
            print(f"   Title: {issue.title}")
            print(f"   State: {issue.state}")
            print(f"   URL: {issue.html_url}")
        except Exception as e:
            print(f"   [ERROR] Failed to fetch issue: {e}")
            return False
    else:
        print("   [SKIP] Skipped")
    print()

    print("=" * 60)
    print("[SUCCESS] GitHub integration is ready!")
    print("=" * 60)
    return True


if __name__ == "__main__":
    success = test_github_integration()
    sys.exit(0 if success else 1)
