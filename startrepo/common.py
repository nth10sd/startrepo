"""Define objects common to all devices."""

from __future__ import annotations

from typing import Self

from overrides import EnforceOverrides  # ty: ignore[unresolved-import]

# class LOSDeviceError(Exception, EnforceOverrides):
#     """Error class unique to LOSDevice objects."""


class LOSDevice(EnforceOverrides):
    """A device that supports Lineage OS.

    :param new_type: This is a new type for LOSDevice
    """

    __slots__: list[str] = ["new_type"]

    def __init__(self, new_type: str) -> None:
        """Initialize the LOSDevice."""
        self.new_type: str = new_type

    @classmethod
    def main(cls: type[Self]) -> None:  # vulture: ignore
        """LOSDevice main method."""

    @staticmethod
    def create() -> str:
        """Build a shell.

        :return: A testing string
        """
        return "FOO"
