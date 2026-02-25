from service.RideService import RideService


class RideManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RideManager, cls).__new__(cls)
            cls._instance._ride_service = RideService()
        return cls._instance

    @property
    def ride_service(self):
        return self._ride_service
