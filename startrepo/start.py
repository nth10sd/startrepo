"""Begin running package code."""

from __future__ import annotations

import logging

from startrepo.common import LOSDevice
from startrepo.util.logging import get_logger
from startrepo.util.utils import add_one

RUN_LOG: logging.Logger = get_logger(__name__)
RUN_LOG.setLevel(logging.INFO)


def main() -> None:
    """Start."""
    _ = LOSDevice("NewType")
    RUN_LOG.warning(add_one(2))
    RUN_LOG.error("foo")
