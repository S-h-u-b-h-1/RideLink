from strategy.PricingStrategy import PricingStrategy


class StandardPricing(PricingStrategy):

    BASE_FARE = 50
    PER_KM_RATE = 10

    def calculate_fare(self, pickup_location, drop_location) -> float:
        distance = pickup_location.distance_to(drop_location)
        fare = self.BASE_FARE + (distance * self.PER_KM_RATE)
        return round(fare, 2)
