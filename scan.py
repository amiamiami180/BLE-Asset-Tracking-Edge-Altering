import asyncio
from bleak import BleakScanner

async def scan_ble_devices():
    print("🔍 Scanning for BLE devices...")
    devices = await BleakScanner.discover(timeout=5.0)
    tag_data = []
    for device in devices:
        print(f"Found {device.address} - RSSI: {device.rssi} dBm")
        tag_data.append((device.address, device.rssi))
    return tag_data

if __name__ == "__main__":
    asyncio.run(scan_ble_devices())






