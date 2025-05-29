import time
from datetime import datetime
from ble_simulator import generate_rssi
from edge_server import check_movement
from mqtt_alert_publisher import send_alert
from config import NUM_TAGS, SIMULATION_STEPS

print("Starting BLE Asset Tracking Simulation\n")

for step in range(SIMULATION_STEPS):
    for tag in range(NUM_TAGS):
        tag_id = f"BLE_TAG_{tag+1}"
        rssi = generate_rssi()
        timestamp = datetime.utcnow().isoformat()
        if check_movement(rssi):
            print(f"[ALERT] {tag_id} moved! RSSI: {rssi} dBm at {timestamp}")
            send_alert(tag_id, rssi, timestamp)
        else:
            print(f"{tag_id}: RSSI = {rssi} dBm")
    time.sleep(1)
