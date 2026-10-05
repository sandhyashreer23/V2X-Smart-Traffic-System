import streamlit as st
import pandas as pd

import plotly.express as px

from traffic_signal import traffic_signal_control
from database import create_database, save_vehicle_data
from emergency_vehicle import check_emergency_vehicle
from traffic_prediction import predict_traffic

from vehicle import Vehicle
from collision_detection import detect_collisions

# Page Settings
st.set_page_config(
    page_title="V2X Smart Traffic System",
    layout="wide"
)

from database import (
    create_database,
    save_vehicle_data,
    get_vehicle_records
)
# Title
st.title("🚗 AI-Based V2X Smart Traffic System")
  
create_database()

# Vehicle Count Slider
vehicle_count = st.slider(
    "Select Number of Vehicles",
    min_value=5,
    max_value=50,
    value=20
)

# Generate Vehicles
vehicles = []

for i in range(vehicle_count):
    vehicle = Vehicle(i + 1)

    vehicle_data = vehicle.get_data()

    vehicles.append(vehicle_data)

    save_vehicle_data(vehicle_data)

# Create DataFrame
df = pd.DataFrame(vehicles)

# Display Vehicle Data
st.subheader("📊 Vehicle Simulation Data")
st.dataframe(df, use_container_width=True)

# Metrics
col1, col2 = st.columns(2)

with col1:
    st.metric("🚗 Total Vehicles", vehicle_count)

with col2:
    avg_speed = round(df["Speed (km/h)"].mean(), 2)
    st.metric("⚡ Average Speed", f"{avg_speed} km/h")

# Map Visualization
st.subheader("🗺️ Live Vehicle Locations")

map_df = df.rename(
    columns={
        "Latitude": "lat",
        "Longitude": "lon"
    }
)

st.map(map_df[["lat", "lon"]])

# Collision Detection
collision_alerts = detect_collisions(vehicles)

st.subheader("⚠️ Collision Alerts")

if collision_alerts:
    alert_df = pd.DataFrame(collision_alerts)
    st.dataframe(alert_df, use_container_width=True)

    st.error(
        f"{len(collision_alerts)} Potential Collision Risk(s) Detected!"
    )
else:
    st.success("✅ No collision risks detected.")

# Traffic Status
# AI Traffic Prediction

# Smart Traffic Signal

st.subheader("🚦 Smart Traffic Signal")

ambulance_detected = st.checkbox("🚑 Ambulance Detected")

signal_status = traffic_signal_control(
    vehicle_count,
    ambulance_detected
)

st.success(signal_status)

if ambulance_detected:
    st.warning("🚑 Emergency Vehicle Alert!")
    st.info("Nearby vehicles have been notified.")
    st.info("Traffic signal changed to GREEN.")

st.subheader("🤖 AI Traffic Prediction")

predicted_status = predict_traffic(
    vehicle_count,
    avg_speed
)

if predicted_status == "Low":
    st.success(f"Predicted Traffic Status: {predicted_status}")

elif predicted_status == "Moderate":
    st.warning(f"Predicted Traffic Status: {predicted_status}")

else:
    st.error(f"Predicted Traffic Status: {predicted_status}")

if vehicle_count < 15:
    traffic_status = "Low Traffic"
elif vehicle_count < 35:
    traffic_status = "Moderate Traffic"
else:
    traffic_status = "High Traffic"

st.info(f"Traffic Status: {traffic_status}")

st.subheader("📈 Traffic Analytics")

fig_speed = px.histogram(
    df,
    x="Speed (km/h)",
    title="Vehicle Speed Distribution",
    nbins=10
)

st.plotly_chart(fig_speed, use_container_width=True)

# Emergency Vehicle Priority

st.subheader("🚑 Emergency Vehicle Priority")

emergency = check_emergency_vehicle()

if emergency:
    st.error(f"{emergency} Detected!")

    st.success("✅ Traffic Signal Turned GREEN")

    st.warning(
        f"⚠️ Nearby Vehicles Alerted: "
        f"Please give way to the {emergency}"
    )
else:
    st.info("No Emergency Vehicle Detected")

st.subheader("🗄️ Stored Vehicle Records")

records = get_vehicle_records()

if records:
    database_df = pd.DataFrame(
        records,
        columns=[
            "Vehicle ID",
            "Speed",
            "Latitude",
            "Longitude",
            "Timestamp"
        ]
    )

    st.dataframe(database_df, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("V2X Smart Traffic & Collision Alert System")