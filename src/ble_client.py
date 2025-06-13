import asyncio
from bleak import BleakScanner, BleakClient
from zone_logic import detect_zone
from mqtt_sender import send_mqtt_alert
from datetime import datetime

TARGET_NAME = "iPhone Amina"
CHAR_UUID = "abcdef00-1234-5678-1234-56789abcdef0"  

last_known_zone = None

def rssi_to_distance(rssi, txPower=-59, n=2):
    """
    Convert RSSI to approximate distance (meters).
    """
    if rssi == 0:
        return -1.0
    ratio = (txPower - rssi) / (10 * n)
    return 10 ** ratio

async def run():
    print("Scanning BLE devices...")
    devices = await BleakScanner.discover()

    target_device = None
    for d in devices:
        rssi = getattr(d, 'rssi', None)
        dist = rssi_to_distance(rssi) if rssi is not None else -1
        print(f"Found: {d.name}, {d.address}, RSSI: {rssi}, Approx. Distance: {dist:.2f} m")
        if d.name and TARGET_NAME in d.name:
            target_device = d
            # Не прерываем цикл, чтобы вывести все устройства (если нужно)
            break

    if not target_device:
        print("Couldn't find iPhone!")
        return

    print(f"Device found: {target_device.name}, connection...")
    async with BleakClient(target_device.address) as client:
        if not client.is_connected:
            print("Failed to connect.")
            return

        print("Connected to GATT server!")

        # Выводим все сервисы и характеристики
        print("\nAvailable services and features:")
        for service in client.services:
            print(f"Service: {service.uuid}")
            for char in service.characteristics:
                print(f"  Characteristic: {char.uuid}, Properties: {char.properties}")

        try:
            value = await client.read_gatt_char(CHAR_UUID)
            print(f"Прочитано значение характеристики ({CHAR_UUID}): {value}")
        except Exception as e:
            print(f"Error reading characteristics {CHAR_UUID}: {e}")
            return

        rssi = getattr(target_device, "rssi", -65)  # fallback
        distance = rssi_to_distance(rssi)
        print(f"RSSI: {rssi} dBm, Approx. Distance: {distance:.2f} м")

        global last_known_zone
        zone = detect_zone(rssi)

        if zone != last_known_zone:
            print(f"Moving: {last_known_zone} → {zone}")
            asset_data = {
                "device": target_device.name,
                "address": target_device.address,
                "zone": zone,
                "rssi": rssi,
                "distance_m": round(distance, 2),
                "timestamp": datetime.now().isoformat()
            }
            send_mqtt_alert(asset_data)
            last_known_zone = zone
        else:
            print(f"Stayed in the zone: {zone}")

if __name__ == "__main__":
    asyncio.run(run())

