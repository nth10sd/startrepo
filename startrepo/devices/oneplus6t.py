"""Code related to a OnePlus 6T."""

from __future__ import annotations

from overrides import (  # ty: ignore[unresolved-import,unused-ignore-comment]
    EnforceOverrides,
)

from startrepo.common import LOSDevice

# class OP6TError(LOSDeviceError, EnforceOverrides):
#     """Error class unique to OP6T objects."""


class OP6T(LOSDevice, EnforceOverrides):
    """OnePlus 6T object."""

    __slots__: list[str] = []

    def __init__(self) -> None:
        """Initialize the OP6T."""
        super().__init__("")

    # @classmethod
    # @override
    # def main(cls) -> None:
    #     """OP6T main method.
    #     """

    # @staticmethod
    # @override
    # def create() -> None:
    #     """Build a shell.
    #     """
