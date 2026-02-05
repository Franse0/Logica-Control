"""
Utility functions for ADW (Agent Development Workflow)
"""

import os
import logging
import random
import string
from datetime import datetime
from pathlib import Path


def make_adw_id() -> str:
    """
    Generate a unique ADW (Agent Development Workflow) ID.
    Format: 7 random alphanumeric characters (e.g., 'a3f9k2m')

    Returns:
        str: Unique ADW ID
    """
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choices(chars, k=7))


def setup_logger(adw_id: str, agent_name: str) -> logging.Logger:
    """
    Setup a logger for an ADW agent that writes to:
    agents/{adw_id}/{agent_name}/execution.log

    Args:
        adw_id: The ADW workflow ID
        agent_name: Name of the agent (e.g., 'adw_plan_build', 'ops')

    Returns:
        logging.Logger: Configured logger instance
    """
    # Determine project root (parent of utils.py)
    project_root = Path(__file__).parent

    # Create log directory
    log_dir = project_root / "agents" / adw_id / agent_name
    log_dir.mkdir(parents=True, exist_ok=True)

    # Create log file path
    log_file = log_dir / "execution.log"

    # Create logger
    logger_name = f"{adw_id}_{agent_name}"
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    # Remove existing handlers to avoid duplicates
    logger.handlers.clear()

    # File handler
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.INFO)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Format
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
