import random
import time
from threading import Thread

import paho.mqtt.client as mqtt
class MyMqttSub(Thread):
    def __init__(self,topic,on_message):
        super().__init__()
        self.on_message = on_message
        self.topic = topic
    def run(self):
        MQTTHOST = "120.46.149.254"
        MQTTPORT = 1883  #
        ClientId = "pycharm" + self.topic+"1"  #
        username = "admin"  #
        password = "public"  #
        mqtt_client = mqtt.Client(ClientId)
        mqtt_client.username_pw_set(username, password)

        def mqtt_connected(mqttClient, userdata, flags, rc):
            print(flags)
            if not rc:
                print("MQTT connect success."+self.topic)
                mqttClient.subscribe(self.topic, qos=0)
            else:
                print("MQTT connect error:", rc)

        mqtt_client.on_connect = mqtt_connected
        mqtt_client.on_message = self.on_message
        mqtt_client.on_subscribe = on_subscribe
        mqtt_client.on_disconnect = on_disconnect
        mqtt_client.connect(MQTTHOST, MQTTPORT, 60)
        mqtt_client.loop_forever()

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscrib topic success,qos = %d" % granted_qos)

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection %s" % rc)