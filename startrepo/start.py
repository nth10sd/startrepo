"""start.py"""

from __future__ import annotations

from logging import INFO as INFO_LOG_LEVEL

from startrepo.common import LOSDevice
from startrepo.util.logging import get_logger
from startrepo.util.utils import add_one

RUN_LOG = get_logger(__name__)
RUN_LOG.setLevel(INFO_LOG_LEVEL)


def main() -> None:
    """main function"""
    LOSDevice("NewType")
    RUN_LOG.warning(add_one(2))
    RUN_LOG.error("foo")
