"""Data types for ADW workflow."""

from typing import Optional, List, Literal
from pydantic import BaseModel, Field


class GitHubIssue(BaseModel):
    """GitHub issue data."""
    number: int
    title: str
    body: Optional[str] = None
    state: str
    html_url: str
    user: dict
    labels: List[dict] = Field(default_factory=list)
    created_at: str
    updated_at: str


class AgentPromptRequest(BaseModel):
    """Request to execute a Claude Code prompt."""
    prompt: str
    adw_id: str
    agent_name: str
    model: str = "sonnet"
    dangerously_skip_permissions: bool = False
    output_file: str


class AgentPromptResponse(BaseModel):
    """Response from Claude Code prompt execution."""
    output: str
    success: bool
    session_id: Optional[str] = None


class AgentTemplateRequest(BaseModel):
    """Request to execute a Claude Code template (slash command)."""
    slash_command: str
    args: List[str] = Field(default_factory=list)
    adw_id: str
    agent_name: str
    model: str = "sonnet"


class ClaudeCodeResultMessage(BaseModel):
    """Result message from Claude Code JSONL output."""
    type: Literal["result"]
    result: str
    is_error: bool = False
    session_id: Optional[str] = None


# Type alias for issue classification slash commands
IssueClassSlashCommand = Literal["/feature", "/bug", "/chore"]
