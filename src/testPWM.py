import LPi.GPIO as GPIO  # 导入LPi.GPIO模块
LED_PIN_LS2K = 13  # 这里选取的是13号引脚
# Test trying to change mode after it has been set
GPIO.setmode(GPIO.LS2K)   # 设置模式
GPIO.setup(LED_PIN_LS2K, GPIO.IN) # 设置一个通道
GPIO.cleanup()   # 清空