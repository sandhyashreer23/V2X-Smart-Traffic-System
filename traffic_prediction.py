from sklearn.ensemble import RandomForestClassifier
import pandas as pd


def train_traffic_model():
    data = pd.DataFrame({
        "vehicle_count": [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
        "avg_speed": [80, 75, 70, 65, 60, 55, 50, 45, 40, 35],
        "traffic_status": [
            "Low",
            "Low",
            "Moderate",
            "Moderate",
            "Moderate",
            "High",
            "High",
            "High",
            "High",
            "High"
        ]
    })

    X = data[["vehicle_count", "avg_speed"]]
    y = data["traffic_status"]

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X, y)

    return model


def predict_traffic(vehicle_count, avg_speed):
    model = train_traffic_model()

    prediction = model.predict([
        [vehicle_count, avg_speed]
    ])

    return prediction[0]