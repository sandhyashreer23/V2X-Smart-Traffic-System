def traffic_signal_control(vehicle_count, ambulance_detected=False):

    if ambulance_detected:
        return "🟢 GREEN SIGNAL - Ambulance Priority"

    if vehicle_count < 15:
        return "🟢 GREEN (Low Traffic)"
    elif vehicle_count < 35:
        return "🟡 YELLOW (Moderate Traffic)"
    else:
        return "🔴 RED (Heavy Traffic)"