from enums.RideStatus import RideStatus


class Ride:
    def __init__(self, ride_id: str, rider, driver, pickup_location, drop_location, fare: float):
        self._ride_id = ride_id
        self._rider = rider
        self._driver = driver
        self._pickup_location = pickup_location
        self._drop_location = drop_location
        self._fare = fare
        self._status = RideStatus.REQUESTED

    @property
    def ride_id(self):
        return self._ride_id

    @property
    def rider(self):
        return self._rider

    @property
    def driver(self):
        return self._driver

    @property
    def status(self):
        return self._status

    @property
    def fare(self):
        return self._fare

    def update_status(self, new_status: RideStatus):
        self._status = new_status

    def __str__(self):
        return (
            f"Ride(id={self._ride_id}, "
            f"rider={self._rider.name}, "
            f"driver={self._driver.name}, "
            f"status={self._status.name}, "
            f"fare={self._fare})"
        )
