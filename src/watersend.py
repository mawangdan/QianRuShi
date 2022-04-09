from MqttClientSend import MyMqttSend
from MqttClientSub import MyMqttSub


def on_message_waterCircle(client, userdata, msg):
    print("主题:",msg.topic," 消息:")
    print(str(msg.payload.decode('utf-8')))
    #这里写接到消息干嘛


def on_message_grassLight(client, userdata, msg):
    print("主题:",msg.topic," 消息:")
    print(str(msg.payload.decode('utf-8')))
    #这里写接到消息干嘛

if __name__ == '__main__':
    m=MyMqttSend()
    #这里传订阅的topic
    m2=MyMqttSub("waterCircle",on_message_waterCircle)
    m3=MyMqttSub("grassLight",on_message_waterCircle())
    #topic,msg
    m.send("waterHeight","王子昂")
    m.send("sad", "王子w昂")