from enum import Enum


class LoadingPlaceLoadingType(str, Enum):
    LOADING = "LOADING"
    UNLOADING = "UNLOADING"

    def __str__(self) -> str:
        return str(self.value)
