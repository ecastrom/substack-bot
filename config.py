"""
config.py — Central configuration
Loads environment variables for Substack, Anthropic, and Telegram APIs.
"""
import os
from dataclasses import dataclass


@dataclass
class SubstackConfig:
    email: str
    password: str
    publication_url: str  # e.g. "edgarcastro.substack.com"


def load_substack_config() -> SubstackConfig:
    return SubstackConfig(
        email=os.environ["SUBSTACK_EMAIL"],
        password=os.environ["SUBSTACK_PASSWORD"],
        publication_url=os.environ.get("SUBSTACK_PUBLICATION_URL", ""),
    )


# Module-level constants for simple env vars
ANTHROPIC_API_KEY: str = os.environ.get("ANTHROPIC_API_KEY", "")
