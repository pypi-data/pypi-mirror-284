import machine
import utime
from machine import Pin, PWM

def zfill(string, width):
    """自定义的左侧填充零函数"""
    if len(string) >= width:
        return string
    else:
        return "0" * (width - len(string)) + string

class IRT(object):

    def __init__(self, gpioNum):
        self.irTransmit = machine.Pin(gpioNum, machine.Pin.OUT)
        self.pwm = PWM(self.irTransmit)
        self.pwm.freq(38000)  # 设置红外发射频率为38kHz
        self.CODE = {
    "*": 1,   # 未知
    "#": 1,   # 未知
    "-": 0xFFE01F,   # 对的
    "+": 0xFFA857,    # 对的
    "EQ": 0xFF906F,   # 对的
    "0": 0xFF6897,     # 对的
    "0": 0xFF6897,    # 对的
    "1": 0xFF30CF,    # 对的
    "2": 0xFF18E7,    # 对的
    "3": 0xFF7A85,    # 对的
    "4": 0xFF10EF,   # 对的
    "5": 0xFF38C7,   # 对的
    "6": 0xFF5AA5,   # 对的
    "7": 0xFF42BD,   # 对的
    "8": 0xFF4AB5,   # 对的
    "9": 0xFF52AD,   # 对的
    "100+": 0xFF9867, # 对的
    "200+": 0xFFB04F,  # 对的
    "ch-": 0xFFA25D,    # 对的
    "ch": 0xFF629D,     # 对的
    "ch+": 0xFFE21D,    # 对的
    "prev": 0xFF22DD,   # 对的
    "next": 0xFF02FD,   # 对的
    "play/stop": 0xFFC23D,  # 对的
    }
    
    def send(self, code):
        """
        发送红外信号
        """
        # 将code转换为二进制
        binary_code = zfill(bin(code)[2:], 32)
        
        # 发送起始信号
        self.pwm.duty(512)
        utime.sleep_us(9000)
        self.pwm.duty(0)
        utime.sleep_us(4500)
        
        # 发送数据
        for bit in binary_code:
            self.pwm.duty(512)
            utime.sleep_us(560)
            self.pwm.duty(0)
            if bit == '1':
                utime.sleep_us(1690)
            else:
                utime.sleep_us(560)
        
        # 发送结束信号
        self.pwm.duty(512)
        utime.sleep_us(560)
        self.pwm.duty(0)
