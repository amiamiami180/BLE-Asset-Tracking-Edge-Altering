# BLE-Asset-Tracking with Edge Alerting
Project on the **Industrial IoT** discipline - tracking the movement of objects using BLE and sending notifications via MQTT.

Project idea
The system tracks objects with BLE tags and sends a warning if the RSSI signal level drops below a specified threshold. This may mean that the tag (and therefore the object) has moved out of the control zone.

The project supports two modes:
- **Simulation** of BLE signals
- **Real work** with BLE devices (via the `bleak` library)

Project structure
BLE-Asset-Tracking-Edge-Alerting/
-requirements.txt
-README.md
-src/
-config.py
-ble_simulator.py
-ble_scanner.py
-edge_server.py
-mqtt_alert_publisher.py
-run_tracking.py

