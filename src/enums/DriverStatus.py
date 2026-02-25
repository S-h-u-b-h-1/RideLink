from enum import Enum


class DriverStatus(Enum):
    AVAILABLE = "AVAILABLE"
    ON_RIDE = "ON_RIDE"
    OFFLINE = "OFFLINE"
