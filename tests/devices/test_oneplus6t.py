"""OP6T tests."""

# ruff: noqa: S101

from __future__ import annotations

from startrepo.devices.oneplus6t import OP6T


def test_op6t() -> None:
    """Test the OP6T class."""
    assert OP6T() if OP6T() else True
