import json
import paho.mqtt.client as mqtt

MQTT_BROKER = "localhost"  # или IP брокера
MQTT_PORT = 1883
MQTT_TOPIC = "iot/ble/alert"

def send_mqtt_alert(data):
    client = mqtt.Client()
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    payload = json.dumps(data)
    client.publish(MQTT_TOPIC, payload)
    client.disconnect()
    print(f"MQTT сообщение отправлено: {payload}")
