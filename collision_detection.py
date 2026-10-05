import math

def calculate_distance(lat1, lon1, lat2, lon2):
    return math.sqrt(
        (lat2 - lat1) ** 2 +
        (lon2 - lon1) ** 2
    )

def detect_collisions(vehicles):
    alerts = []

    for i in range(len(vehicles)):
        for j in range(i + 1, len(vehicles)):

            v1 = vehicles[i]
            v2 = vehicles[j]

            distance = calculate_distance(
                v1["Latitude"],
                v1["Longitude"],
                v2["Latitude"],
                v2["Longitude"]
            )

            if distance < 0.02:
                alerts.append({
                    "Vehicle A": v1["Vehicle ID"],
                    "Vehicle B": v2["Vehicle ID"],
                    "Distance": round(distance, 4),
                    "Alert": "⚠ Collision Risk"
                })

    return alerts
