import asyncio
from bleak import BleakClient, BleakScanner

# UUID сервиса и характеристики с iPhone
SERVICE_UUID = "12345678-1234-5678-1234-56789ABCDE0"
CHAR_UUID = "ABCDEF01-1234-5678-1234-56789ABCDE0"


TARGET_NAME = "iPhone Amina"
TARGET_ADDRESS = "5CA05517-D577-42F7-3F68-120D5A0AEA44"  # тоже можешь использовать

async def run():
    print("Scanning BLE devices...")
    devices = await BleakScanner.discover()
    
    target_device = None
    for d in devices:
        print(f"Found: {d.name}, {d.address}, RSSI: {d.rssi}")
        if d.address == TARGET_ADDRESS or (d.name and TARGET_NAME in d.name):
            target_device = d
            break
    
    if not target_device:
        print("Couldn't find iPhone!")
        return
    
    print(f"Connecting to {target_device.name}...")
    async with BleakClient(target_device.address) as client:
        connected = await client.is_connected()
        print(f"Connected: {connected}")
        
        try:
            value = await client.read_gatt_char(CHAR_UUID)
            print(f"Read value of the characteristic: {value}")
        except Exception as e:
            print(f"Error reading characteristics: {e}")

asyncio.run(run())



