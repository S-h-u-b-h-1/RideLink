from strategy.PricingStrategy import PricingStrategy


class SurgePricing(PricingStrategy):

    BASE_FARE = 50
    PER_KM_RATE = 10

    def __init__(self, surge_multiplier: float):
        self._surge_multiplier = surge_multiplier

    def calculate_fare(self, pickup_location, drop_location) -> float:
        distance = pickup_location.distance_to(drop_location)
        normal_fare = self.BASE_FARE + (distance * self.PER_KM_RATE)
        surged_fare = normal_fare * self._surge_multiplier
        return round(surged_fare, 2)
