
from machine import Pin,I2C
#from machine import Pin,SoftI2C #软I2C
 
COMMAND_I2C_ADDRESS = 0x24  # 对应数码管I2C地址[36, 37, 38, 39, 52, 53, 54, 55]的36
DISPLAY_I2C_ADDRESS = 0x34  # 对应数码管I2C地址[36, 37, 38, 39, 52, 53, 54, 55]的52
 
# 对应单个数码管的0到F显示。0不亮1亮。例如0x3F二进制为0011 1111，高位dp，地位为a,对应8段数码管则显示为0
buf = (0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x6F,0x77,0x7C,0x39,0x5E,0x79,0x71)  
 
i2c = I2C(1)
#i2c = SoftI2C(scl=Pin(25), sda=Pin(26)) #软I2C
# FDD FourDigitDisplay
class FDD():
    def __init__(self):
        self._intensity = 3
        self.dbuf = [0, 0, 0, 0]
        self.tbuf = bytearray(1)
        self.on()
 
    def intensity(self, dat = -1):
        if dat < 0 or dat > 8:
            return self._intensity
        if dat == 0:
            self.off()
        else:
            self._intensity = dat
            self.cmd((dat<<4)|0x01)
 
    def cmd(self, c):
        self.tbuf[0] = c
        i2c.writeto(COMMAND_I2C_ADDRESS, self.tbuf)
 
    def dat(self, bit, d):
        self.tbuf[0] = d
        i2c.writeto(DISPLAY_I2C_ADDRESS + (bit%4), self.tbuf)
 
    def on(self):
        self.cmd((self._intensity<<4)|0x01)
 
    def off(self):
        self._intensity = 0
        self.cmd(0)
 
    def clear(self):
        self.dat(0, 0)
        self.dat(1, 0)
        self.dat(2, 0)
        self.dat(3, 0)
        self.dbuf = [0, 0, 0, 0]
 
    def showbit(self, num, bit = 0):
        self.dbuf[bit%4] = buf[num%16]
        self.dat(bit, buf[num%16])
 
    def shownum(self, num):
        if num < 0:
            self.dat(0, 0x40)   # '-'
            num = -num
        else:
            self.showbit((num // 1000) % 10)
        self.showbit(num % 10, 3)
        self.showbit((num // 10) % 10, 2)
        self.showbit((num // 100) % 10, 1)
 
    def showhex(self, num):
        if num < 0:
            self.dat(0, 0x40)   # '-'
            num = -num
        else:
            self.showbit((num >> 12) % 16)
        self.showbit(num % 16, 3)
        self.showbit((num >> 4) % 16, 2)
        self.showbit((num >> 8) % 16, 1)
 
    def showDP(self, bit = 1, show = True):
        if show:
            self.dat(bit, self.dbuf[bit] | 0x80)
        else:
            self.dat(bit, self.dbuf[bit] & 0x7F)
            
    def showfloat(self,num,point):
        new = int(num*(10**point))
        self.shownum(new)
        self.showDP(3-point)
