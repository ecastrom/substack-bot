"""
config.py — Central configuration
Loads environment variables for Substack, Anthropic, and Telegram APIs.
"""
import os
from dataclasses import dataclass


@dataclass
class SubstackConfig:
    session_cookie: str  # substack.sid cookie value


def load_substack_config() -> SubstackConfig:
    return SubstackConfig(
        session_cookie=os.environ["SUBSTACK_SESSION_COOKIE"],
    )


# Module-level constants for simple env vars
ANTHROPIC_API_KEY: str = os.environ.get("ANTHROPIC_API_KEY", "")
