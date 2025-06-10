import asyncio
from bleak import BleakGATTCharacteristic, BleakGATTService, BleakGATTServer

from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData

class CustomServer(BleakGATTServer):
    def __init__(self):
        super().__init__()
        self.rssi_value = -75  # можно обновлять по сканированию

        self.service = BleakGATTService("12345678-1234-5678-1234-56789abcdef0")
        self.characteristic = BleakGATTCharacteristic(
            "12345678-1234-5678-1234-56789abcdef1",
            ["read"],
        )

        self.characteristic.read = self.read_rssi
        self.service.add_characteristic(self.characteristic)
        self.add_service(self.service)

    async def read_rssi(self, characteristic, **kwargs):
        value = int.to_bytes(self.rssi_value, length=1, byteorder='little', signed=True)
        return value

async def main():
    server = CustomServer()
    await server.start()
    print("GATT Server started. Waiting for connections...")

    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        print("Stopping server.")
        await server.stop()

if __name__ == "__main__":
    asyncio.run(main())
