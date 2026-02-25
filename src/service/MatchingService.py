class MatchingService:

    @staticmethod
    def find_nearest_driver(rider_location, drivers: list):
        """
        Returns the nearest AVAILABLE driver.
        """

        nearest_driver = None
        min_distance = float("inf")

        for driver in drivers:
            if driver.is_available():
                distance = driver.location.distance_to(rider_location)

                if distance < min_distance:
                    min_distance = distance
                    nearest_driver = driver

        return nearest_driver
