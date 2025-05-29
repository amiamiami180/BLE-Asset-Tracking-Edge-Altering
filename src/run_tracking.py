import asyncio
import time
from datetime import datetime
from edge_server import check_movement
from mqtt_alert_publisher import send_alert
from ble_scanner import scan_ble_devices
from config import RSSI_THRESHOLD

print("Starting Real BLE Asset Tracking\n")

async def main():
    while True:
        tag_data = await scan_ble_devices()
        for tag_id, rssi in tag_data:
            timestamp = datetime.utcnow().isoformat()
            if check_movement(rssi):
                print(f"[ALERT] {tag_id} moved! RSSI: {rssi} dBm at {timestamp}")
                send_alert(tag_id, rssi, timestamp)
            else:
                print(f"{tag_id}: RSSI = {rssi} dBm")
        time.sleep(3)

asyncio.run(main())

