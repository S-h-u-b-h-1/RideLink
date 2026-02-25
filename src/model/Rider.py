class Rider:
    def __init__(self, rider_id: str, name: str, location):
        self._rider_id = rider_id
        self._name = name
        self._location = location

    @property
    def rider_id(self):
        return self._rider_id

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    def update_location(self, new_location):
        self._location = new_location

    def __str__(self):
        return f"Rider(id={self._rider_id}, name={self._name})"
