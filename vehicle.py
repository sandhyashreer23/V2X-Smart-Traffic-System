import random

class Vehicle:
    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id
        self.speed = random.randint(40, 100)  # km/h
        self.latitude = round(random.uniform(12.90, 13.10), 4)
        self.longitude = round(random.uniform(77.50, 77.70), 4)

    def get_data(self):
        return {
            "Vehicle ID": self.vehicle_id,
            "Speed (km/h)": self.speed,
            "Latitude": self.latitude,
            "Longitude": self.longitude
        }