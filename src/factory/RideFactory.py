import uuid
from model.ride import Ride


class RideFactory:

    @staticmethod
    def create_ride(rider, driver, pickup_location, drop_location, pricing_strategy):
        """
        Creates a Ride object after calculating fare using given strategy
        """
        ride_id = str(uuid.uuid4())
        fare = pricing_strategy.calculate_fare(pickup_location, drop_location)

        return Ride(
            ride_id=ride_id,
            rider=rider,
            driver=driver,
            pickup_location=pickup_location,
            drop_location=drop_location,
            fare=fare
        )
