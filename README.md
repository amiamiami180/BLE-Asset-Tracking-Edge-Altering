# BLE-Asset-Tracking
This project implements a Bluetooth Low Energy (BLE)-based asset tracking system with edge alerting logic, combining real-time signal strength processing and MQTT-based communication. The system demonstrates how to perform coarse localization using RSSI (Received Signal Strength Indicator) and respond to changes via Simulink logic blocks.

# Features
- Scanning of real BLE devices using Python and the `bleak` library
- MQTT-based data transmission
- Real-time RSSI, zone, and distance processing in MATLAB
- Simulation in Simulink, including visualization and alert logic
- Edge alerting based on thresholds and zone information

# Processing Logic
RSSI is used to estimate distance to the BLE device.
Alerts can be triggered when RSSI drops below a certain threshold.
The zone parameter indicates the logical location (e.g., entry, hallway, exit).
Simulink blocks can trigger alarms or set flags for edge events.

# Technologies Used
MATLAB/Simulink: Simulation and real-time signal logic
Python: BLE scanning and MQTT data publishing
MQTT (paho):	Lightweight communication protocol
Bleak (Python):	BLE scanning on macOS/Linux/Windows


