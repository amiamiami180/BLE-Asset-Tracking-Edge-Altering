from config import RSSI_THRESHOLD

def check_movement(rssi):
    return rssi < RSSI_THRESHOLD
