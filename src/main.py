from model.Location import Location
from model.Rider import Rider
from model.Driver import Driver
from strategy.StandardPricing import StandardPricing
from strategy.SurgePricing import SurgePricing
from singleton.RideManager import RideManager


def main():
    # Create locations
    rider_location = Location(10, 10)
    driver1_location = Location(12, 12)
    driver2_location = Location(8, 9)

    # Create rider
    rider = Rider("R1", "Shubhaang", rider_location)

    # Create drivers
    driver1 = Driver("D1", "Rahul", driver1_location)
    driver2 = Driver("D2", "Amit", driver2_location)

    drivers = [driver1, driver2]

    # Choose pricing strategy
    pricing_strategy = StandardPricing()
    # pricing_strategy = SurgePricing(1.5)   # Uncomment to test surge pricing

    # Get singleton RideManager
    manager = RideManager()

    try:
        ride = manager.ride_service.request_ride(
            rider=rider,
            pickup_location=rider_location,
            drop_location=Location(20, 20),
            drivers=drivers,
            pricing_strategy=pricing_strategy
        )

        print("Ride successfully created!")
        print(ride)

    except Exception as e:
        print("Error:", e)

    manager.ride_service.accept_ride(ride)
    print("Ride Accepted:", ride.status.name)

    manager.ride_service.start_ride(ride)
    print("Ride Started:", ride.status.name)

    manager.ride_service.complete_ride(ride)
    print("Ride Completed:", ride.status.name)

if __name__ == "__main__":
    main()
