import time

import paho.mqtt.client as mqtt

class MyMqttSend():
    def __init__(self):
        self.MQTTHOST = "120.46.149.254"
        self.MQTTPORT = 1883
        self.ClientId = "pycharm" + str(time.time())
        self.username = "admin"
        self.password = "public"
        self.mqtt_client = mqtt.Client(self.ClientId)
        self.mqtt_client.username_pw_set(self.username, self.password)
        self.mqtt_client.on_connect = mqtt_connected
        self.mqtt_client.on_message = on_message
        self.mqtt_client.on_subscribe = on_subscribe
        self.mqtt_client.on_disconnect = on_disconnect
        self.mqtt_client.connect(self.MQTTHOST, self.MQTTPORT, 60)
    def send(self,topic,msg):
        self.mqtt_client.publish(topic, msg, qos=0)
        print(topic+msg)


def mqtt_connected(mqttClient, userdata, flags,rc):
    print(flags)
    if not rc:
        print("MQTT connect success.")
        #mqttClient.subscribe("Python_publish", qos=0)
        mqttClient.publish("Python_publish", "1", qos=0)

    else:
        print("MQTT connect error:", rc)


def on_message(client, userdata, msg):
    print("主题:",msg.topic," 消息:")
    print(str(msg.payload.decode('utf-8')))

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscrib topic success,qos = %d" % granted_qos)

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection %s" % rc)

