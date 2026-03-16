from enum import Enum


class ClosedFreightExchangePublicationType(str, Enum):
    EXTERNAL_LATER = "EXTERNAL_LATER"
    INTERNAL_ONLY = "INTERNAL_ONLY"

    def __str__(self) -> str:
        return str(self.value)
