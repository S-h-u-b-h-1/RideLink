from enums.driver_status import DriverStatus


class Driver:
    def __init__(self, driver_id: str, name: str, location):
        self._driver_id = driver_id
        self._name = name
        self._location = location
        self._status = DriverStatus.AVAILABLE

    @property
    def driver_id(self):
        return self._driver_id

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    @property
    def status(self):
        return self._status

    def update_location(self, new_location):
        self._location = new_location

    def set_status(self, status: DriverStatus):
        self._status = status

    def is_available(self):
        return self._status == DriverStatus.AVAILABLE

    def __str__(self):
        return f"Driver(id={self._driver_id}, name={self._name}, status={self._status.name})"
