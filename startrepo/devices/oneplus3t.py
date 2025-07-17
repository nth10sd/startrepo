"""Code related to a OnePlus 3T."""

from __future__ import annotations

from overrides import EnforceOverrides

from startrepo.common import LOSDevice

# class OP3TError(LOSDeviceError, EnforceOverrides):
#     """Error class unique to OP3T objects."""


class OP3T(LOSDevice, EnforceOverrides):
    """OnePlus 3T object."""

    __slots__: list[str] = []

    def __init__(self) -> None:
        """Initialize the OP3T."""
        super().__init__("")

    def __bool__(self) -> bool:
        """Behave meaningfully in boolean contexts."""
        return bool(0)  # For the OnePlus 3T object

    # @classmethod
    # @override
    # def main(cls) -> None:
    #     """OP3T main method.
    #     """

    # @staticmethod
    # @override
    # def create() -> None:
    #     """Build a shell.
    #     """
