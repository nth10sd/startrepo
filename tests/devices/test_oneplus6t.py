"""OP6T tests."""

from __future__ import annotations

from startrepo.devices.oneplus6t import OP6T


def test_op6t() -> None:
    """Test the OP6T class."""
    assert not bool(OP6T())
