import asyncio
from bleak import BleakScanner

# Пороговое значение сигнала для срабатывания тревоги
RSSI_THRESHOLD = -70  # dBm

async def scan_ble_devices():
    print("Scanning for BLE devices...")
    devices = await BleakScanner.discover(timeout=5.0)
    if not devices:
        print("No BLE devices found.")
    tag_data = []
    for device in devices:
        print(f"Found {device.address} - RSSI: {device.rssi} dBm")
        tag_data.append((device.address, device.rssi))
    return tag_data

async def main():
    print("Starting Real BLE Asset Tracking\n")
    for _ in range(5):  # Повторяем сканирование 5 раз
        tag_data = await scan_ble_devices()
        for address, rssi in tag_data:
            if rssi >= RSSI_THRESHOLD:
                print(f"ALERT: Device {address} is too close! (RSSI: {rssi} dBm)")
        print("-" * 40)
        await asyncio.sleep(3)  # Пауза между сканированиями

if __name__ == "__main__":
    asyncio.run(main())

 

