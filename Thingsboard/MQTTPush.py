# pip install paho-mqtt
############## Pub ####################
import paho.mqtt.client as mqtt

# *********************************************************************
# MQTT Config

MQTT_SERVER = "172.16.10.200"
MQTT_PORT = 1883
MQTT_ALIVE = 60
MQTT_TOPIC1 = "v1/devices/me/telemetry"
ACCESS_TOKEN = "IUlSwXUL2WoYp414q6Fx"
# *********************************************************************

mqtt_client = mqtt.Client()
mqtt_client.username_pw_set(ACCESS_TOKEN)
mqtt_client.connect(MQTT_SERVER, MQTT_PORT, MQTT_ALIVE)
mqtt_client.loop_start()

import time
import json
import random
import math

# The retain flag is used to Let other side to get back the result once connect
# mqtt_client.publish(topic=MQTT_TOPIC1, payload=json.dumps(payload), qos=1, retain=False)

try:
        while True:

                myTime = time.asctime( time.localtime(time.time()) )
                myVal = 20*math.sin(2*math.pi*(1/(60))*time.time())+5*math.sin(2*math.pi*(3/60)*time.time())
#               print(myVal)
                payload = {"time": myTime, "value": myVal}

                mqtt_client.publish(topic=MQTT_TOPIC1, payload=json.dumps(payload), qos=2)
                time.sleep(1)

except KeyboardInterrupt:
        pass

mqtt_client.loop_stop()
mqtt_lient.disconnect()
