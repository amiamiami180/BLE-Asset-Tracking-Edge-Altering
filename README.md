# BLE-Asset-Tracking
This project is part of the **Industrial IoT** course and demonstrates a basic asset tracking system using **Bluetooth Low Energy (BLE)**, with **edge alerting** capabilities and **MQTT** integration.
Features

- Simulates BLE RSSI signals
- Detects asset movement based on RSSI threshold
- Sends MQTT alerts to a broker
- (Optional) Interacts with real BLE devices using `bleak`
  
  Project Structure

BLE-Asset-Tracking-Edge-Alerting/
├── requirements.txt
└── src/
├── config.py
├── ble_simulator.py
├── edge_server.py
├── mqtt_alert_publisher.py
└── run_tracking.py
