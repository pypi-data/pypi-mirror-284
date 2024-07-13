"""A rich CLI tool for network device reconnaissance."""

from typing import Any

__all__ = []


def export(defn: Any) -> None:  # noqa: ANN401
    """Module-level export decorator."""
    globals()[defn.__name__] = defn
    __all__.append(defn.__name__)  # noqa: PYI056
    return defn


__copyright__ = "Copyright (c) 2024 ReK42"
from netrecon._version import __version__
from netrecon.__main__ import main
