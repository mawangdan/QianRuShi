import time

import paho.mqtt.client as mqtt
def mqtt_connected(mqttClient, userdata, flags,rc):
    print(flags)
    if not rc:
        print("MQTT connect success.")
        mqttClient.subscribe("Python_publish", qos=0)  # 订阅主题

    else:
        print("MQTT connect error:", rc)


# 收到订阅主题数据回调函数
def on_message(client, userdata, msg):
    print("主题:",msg.topic," 消息:")
    print(str(msg.payload.decode('utf-8')))

# 订阅主题成功回调函数
def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscrib topic success,qos = %d" % granted_qos)

# 失去连接回调函数
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection %s" % rc)



if __name__ == '__main__':
    MQTTHOST = "120.46.149.254"  # MQTT服务器的IP地址
    MQTTPORT = 1883  # MQTT服务器的端口号
    ClientId = "pycharm" + str(time.time())  # ClientId需要唯一
    username = "admin"  # 用户名
    password = "public"  # 用户名对应的密码
    mqtt_client = mqtt.Client(ClientId)
    mqtt_client.username_pw_set(username, password)
    mqtt_client.on_connect = mqtt_connected  # 设置连接成功回调函数
    mqtt_client.on_message = on_message  # 设置收到订阅主题数据回调函数
    mqtt_client.on_subscribe = on_subscribe  # 设置订阅主题成功回调函数
    mqtt_client.on_disconnect = on_disconnect  # 设置失去连接回调函数
    mqtt_client.connect(MQTTHOST, MQTTPORT, 60)
    # 网络循环的阻塞形式，直到客户端调用disconnect()时才会返回。它会自动处理重新连接
    mqtt_client.loop_forever()