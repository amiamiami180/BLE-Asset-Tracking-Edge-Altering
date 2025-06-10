import asyncio
import math
from bleak import BleakScanner

# Функция оценки расстояния по RSSI
def estimate_distance(rssi, tx_power=-59):
    if rssi == 0:
        return None
    ratio = rssi / tx_power
    if ratio < 1.0:
        return round(pow(ratio, 10), 2)
    else:
        return round(0.89976 * pow(ratio, 7.7095) + 0.111, 2)

# Асинхронный сканер BLE
async def scan_ble_devices():
    print("Scanning for BLE devices...")
    devices = await BleakScanner.discover(timeout=5.0)

    if not devices:
        print("No BLE devices found.")
        return

    for device in devices:
        distance = estimate_distance(device.rssi)
        print(f"Found {device.address} | RSSI: {device.rssi} dBm | Estimated distance: {distance} m")

        # Проверка на близость
        if distance and distance < 1.0:
            print(f"ALERT: {device.address} is TOO CLOSE ({distance} m)!")

# Запуск сканирования
if __name__ == "__main__":
    asyncio.run(scan_ble_devices())







