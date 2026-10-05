import random


def check_emergency_vehicle():
    emergency_types = [
        "Ambulance",
        "Police",
        "Fire Truck",
        None
    ]

    return random.choice(emergency_types)