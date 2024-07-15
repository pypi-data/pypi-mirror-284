"""Schema definition for the agent."""
from enum import Enum


class PluginStorageType(Enum):
    """Plugin storage type."""

    Git = "git"
    Oss = "oss"


class ApiTagType(Enum):
    """API tag type."""

    API_VIEW = "gptdb_view"
    API_CALL = "gptdb_call"


class Status(Enum):
    """Status of a task."""

    TODO = "todo"
    RUNNING = "running"
    WAITING = "waiting"
    RETRYING = "retrying"
    FAILED = "failed"
    COMPLETE = "complete"
