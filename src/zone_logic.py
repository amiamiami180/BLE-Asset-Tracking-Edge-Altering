# zone_logic.py

def detect_zone(rssi: int) -> str:
    if rssi >= -50:
        return "Zone A - Very Close"
    elif -70 <= rssi < -50:
        return "Zone B - Nearby"
    elif -90 <= rssi < -70:
        return "Zone C - Far"
    else:
        return "Zone Unknown"

def estimate_distance(rssi: int) -> float:
    """
    Приблизительная оценка расстояния на основе RSSI.
    """
    tx_power = -59  # мощность сигнала на расстоянии 1 метр (настраивается)
    if rssi == 0:
        return -1.0  # неизвестно
    ratio = rssi / tx_power
    if ratio < 1.0:
        return round(ratio**10, 2)
    else:
        return round((0.89976 * ratio**7.7095 + 0.111), 2)


