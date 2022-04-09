import time
from loongpio import LED
GPIO.setmode(GPIO.LS2K)
import paho.mqtt.client as mqtt
def mqtt_connected(mqttClient, userdata, flags,rc):
    print(flags)
    if not rc:
        print("MQTT connect success.")
        mqttClient.subscribe("waterHeight", qos=0)

    else:
        print("MQTT connect error:", rc)


def on_message(client, userdata, msg):
    print("主题:",msg.topic," 消息:")
    print(str(msg.payload.decode('utf-8')))
    msg=str(msg.payload.decode('utf-8'))
    if msg=="0":
        led=LED(7)
        led.on()
    if msg=="1":
        led = LED(7)
        led.off()
def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscrib topic success,qos = %d" % granted_qos)

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection %s" % rc)



if __name__ == '__main__':
    MQTTHOST = "120.46.149.254"
    MQTTPORT = 1883  #
    ClientId = "pycharm" + str(time.time())  #
    username = "admin"  #
    password = "public"  #
    mqtt_client = mqtt.Client(ClientId)
    mqtt_client.username_pw_set(username, password)
    mqtt_client.on_connect = mqtt_connected
    mqtt_client.on_message = on_message
    mqtt_client.on_subscribe = on_subscribe
    mqtt_client.on_disconnect = on_disconnect
    mqtt_client.connect(MQTTHOST, MQTTPORT, 60)
    mqtt_client.loop_forever()