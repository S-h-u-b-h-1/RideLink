from abc import ABC, abstractmethod


class PricingStrategy(ABC):

    @abstractmethod
    def calculate_fare(self, pickup_location, drop_location) -> float:
        pass
