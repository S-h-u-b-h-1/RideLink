import math


class Location:
    def __init__(self, latitude: float, longitude: float):
        self._latitude = latitude
        self._longitude = longitude

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    def distance_to(self, other: "Location") -> float:
        """
        Simple Euclidean distance.
        (Can be replaced with Haversine formula later)
        """
        lat_diff = self._latitude - other.latitude
        lon_diff = self._longitude - other.longitude
        return math.sqrt(lat_diff ** 2 + lon_diff ** 2)
