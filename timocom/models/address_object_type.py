from enum import Enum


class AddressObjectType(str, Enum):
    ADDRESS = "address"
    POSTALADDRESS = "postalAddress"

    def __str__(self) -> str:
        return str(self.value)
