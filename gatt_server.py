import asyncio
from bleak import BleakGATTServer

SERVICE_UUID = "12345678-1234-5678-1234-56789abcdef0"
CHAR_UUID = "12345678-1234-5678-1234-56789abcdef1"

async def run_server():
    server = BleakGATTServer()

    # Добавляем сервис
    service = server.add_service(SERVICE_UUID)

    # Добавляем характеристику с начальным значением -75
    characteristic = service.add_characteristic(CHAR_UUID, 
properties=["read"])
    characteristic.value = bytearray([-75 & 0xFF])

    print("🔗 GATT Server started. Waiting for connections...")
    await server.start()

    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        print("Stopping server...")
    finally:
        await server.stop()

if __name__ == "__main__":
    asyncio.run(run_server())

