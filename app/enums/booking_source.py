from enum import Enum


class BookingSource(str, Enum):
    DIRECT = "direct"
    OTA = "ota"
    PMS = "pms"
    WALK_IN = "walkin"
