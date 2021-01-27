# pip install paho-mqtt
############## Pub ####################
import paho.mqtt.client as mqtt
import json

# *********************************************************************
# MQTT Config

MQTT_SERVER = "172.16.10.200"
MQTT_PORT = 1883
MQTT_ALIVE = 60
MQTT_TOPIC1 = "v1/devices/me/telemetry"
ACCESS_TOKEN = "ABCDEFGHIJK"
# *********************************************************************

mqtt_client = mqtt.Client()
mqtt_client.username_pw_set(ACCESS_TOKEN)
mqtt_client.connect(MQTT_SERVER, MQTT_PORT, MQTT_ALIVE)
mqtt_client.loop_start()

# The retain flag is used to Let other side to get back the result once connect
# mqtt_client.publish(topic=MQTT_TOPIC1, payload=json.dumps(payload), qos=1, retain=False)

# payload = {"time": myTime, "value": myVal}
# mqtt_client.publish(topic=MQTT_TOPIC1, payload=json.dumps(payload), qos=2)

def thingsboard_push(payload):
    """
    nowTime = time.time()
		if nowTime - tb_time > 2:
			myTime = time.asctime( time.localtime(time.time()) )
			tb.thingsboard_push({"time": myTime, "value": count})
			tb_time = nowTime
    """
    mqtt_client.publish(topic=MQTT_TOPIC1, payload=json.dumps(payload), qos=2)
