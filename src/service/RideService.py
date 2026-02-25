from service.MatchingService import MatchingService
from factory.RideFactory import RideFactory
from enums.DriverStatus import DriverStatus


class RideService:

    def __init__(self):
        self._rides = []   # simple in-memory storage

    def request_ride(self, rider, pickup_location, drop_location, drivers, pricing_strategy):
        """
        Complete ride booking workflow
        """

        # Step 1: Find nearest driver
        driver = MatchingService.find_nearest_driver(pickup_location, drivers)

        if not driver:
            raise Exception("No available drivers nearby.")

        # Step 2: Create ride using Factory
        ride = RideFactory.create_ride(
            rider=rider,
            driver=driver,
            pickup_location=pickup_location,
            drop_location=drop_location,
            pricing_strategy=pricing_strategy
        )

        # Step 3: Update driver status
        driver.set_status(DriverStatus.ON_RIDE)

        # Step 4: Store ride
        self._rides.append(ride)

        return ride

    def get_all_rides(self):
        return self._rides
