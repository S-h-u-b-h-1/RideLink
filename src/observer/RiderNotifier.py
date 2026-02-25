from observer.Observer import Observer


class RiderNotifier(Observer):

    def update(self, ride):
        print(f"[Notification to Rider {ride.rider.name}] "
              f"Ride status changed to {ride.status.name}")