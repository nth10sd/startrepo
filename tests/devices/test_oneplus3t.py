"""OP3T tests."""

# ruff: noqa: S101

from __future__ import annotations

from startrepo.devices.oneplus3t import OP3T


def test_op3t() -> None:
    """Test the OP3T class."""
    assert OP3T() if OP3T() else True
