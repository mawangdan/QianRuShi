import random
import time
import LPi.GPIO as GPIO
from time import sleep
from MqttClientSend import MyMqttSend
from MqttClientSub import MyMqttSub



def on_message_waterCircle(client, userdata, msg):
    print("主题:",msg.topic," 消息:")
    print(str(msg.payload.decode('utf-8')))
    msg=str(msg.payload.decode('utf-8'))
    #这里写接到消息干嘛,主要是使水循环开启
    if(msg=="0"):
        GPIO.setup(7, GPIO.OUT)
        GPIO.output(7, 0 )

    elif(msg=="1"):
        GPIO.setup(7, GPIO.OUT)
        GPIO.output(7, 1)



def on_message_grassLight(client, userdata, msg):
    print("主题:",msg.topic," 消息:")
    print(str(msg.payload.decode('utf-8')))
    #这里写接到消息干嘛，主要是使水草灯光开启
    msg = str(msg.payload.decode('utf-8'))
    if (msg == "0"):
        GPIO.setup(2, GPIO.OUT)
        GPIO.output(2, 0)
    elif (msg == "1"):
        GPIO.setup(2, GPIO.OUT)
        GPIO.output(2, 1)

def on_message_food(client, userdata, msg):
    print("主题:",msg.topic," 消息:")
    print(str(msg.payload.decode('utf-8')))
    #这里写接到消息干嘛，主要投喂一次
    msg = str(msg.payload.decode('utf-8'))
    if (msg == "1"):
        GPIO.setup(3, GPIO.OUT)
        GPIO.output(3, 1)
        sleep(20)
        GPIO.output(3, 0)


def on_message_douyu(client, userdata, msg):
    print("主题:",msg.topic," 消息:")
    print(str(msg.payload.decode('utf-8')))
    #这里写接到消息干嘛，主要是使逗鱼的电机开启
    msg = str(msg.payload.decode('utf-8'))
    if (msg == "0"):
        pass
    elif (msg == "1"):
        pass

if __name__ == '__main__':
    #这里传订阅的topic
    GPIO.setmode(GPIO.LS2K)
    m2=MyMqttSub("waterCircleCtrl",on_message_waterCircle)
    m2.start()
    m3=MyMqttSub("grassLightCtrl",on_message_grassLight)
    m3.start()
    m4 = MyMqttSub("foodCtrl", on_message_food)
    m4.start()
    m5 = MyMqttSub("douyu", on_message_douyu)
    m5.start()


    # m1=MyMqttSend()
    # while True:
    #     #10s更新一次信息
    #     #这里通过IO读入信息
    #     # topic,msg
    #     m1.send("waterHeight", str(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])))
    #     time.sleep(0.2)
    #     m1.send("foodLast", str(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])))
    #     time.sleep(0.2)
    #     m1.send("waterTemp", str(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])))
    #     time.sleep(0.2)
    #     m1.send("grassLight", str(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])))
    #     time.sleep(0.2)

