import sqlite3
from datetime import datetime


def create_database():
    conn = sqlite3.connect("traffic_data.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vehicles (
        vehicle_id INTEGER,
        speed REAL,
        latitude REAL,
        longitude REAL,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_vehicle_data(vehicle):
    conn = sqlite3.connect("traffic_data.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO vehicles
    (vehicle_id, speed, latitude, longitude, timestamp)
    VALUES (?, ?, ?, ?, ?)
    """, (
        vehicle["Vehicle ID"],
        vehicle["Speed (km/h)"],
        vehicle["Latitude"],
        vehicle["Longitude"],
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


def get_vehicle_records():
    conn = sqlite3.connect("traffic_data.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM vehicles")

    records = cursor.fetchall()

    conn.close()

    return records