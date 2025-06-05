import paho.mqtt.client as mqtt
import json
from config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC

def send_alert(tag_id, rssi, timestamp):
    client = mqtt.Client()
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    payload = {
        "alert": "Asset moved!",
        "tag_id": tag_id,
        "rssi": rssi,
        "timestamp": timestamp
    }
    client.publish(MQTT_TOPIC, json.dumps(payload))
    client.disconnect()
