"""
Initializing the Python package
"""

from .auth import detect_type, auth, token
from .users import get
from .model import BaseUser


__version__ = "0.11"

__all__ = (
    "__version__",
    "detect_type",
    "auth",
    "token",
    "get",
    "BaseUser",
)
