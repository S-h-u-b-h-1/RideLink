from observer.Observer import Observer


class DriverNotifier(Observer):

    def update(self, ride):
        print(f"[Notification to Driver {ride.driver.name}] "
              f"Ride status changed to {ride.status.name}")