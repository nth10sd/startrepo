"""Code related to a OnePlus 6T."""

from __future__ import annotations

from overrides import EnforceOverrides

from startrepo.common import LOSDevice

# class OP6TError(LOSDeviceError, EnforceOverrides):
#     """Error class unique to OP6T objects."""


class OP6T(LOSDevice, EnforceOverrides):
    """OnePlus 6T object."""

    __slots__: list[str] = []

    def __init__(self) -> None:
        """Initialize the OP6T."""
        super().__init__("")

    def __bool__(self) -> bool:
        """Behave meaningfully in boolean contexts."""
        return bool(0)  # Change to self.name of the OnePlus 6T object when added

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
