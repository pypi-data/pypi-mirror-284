from machine import Pin, I2C
import time
print('传感器默认scl为22引脚，sda为21引脚')
i2c = I2C(-1,Pin(22),Pin(21),freq=100000)
addr = 0x5a
def ldtemp():
    room = i2c.readfrom_mem(addr, 0x06, 2) 
    human = i2c.readfrom_mem(addr, 0x07, 2) 
    room = room[1]*256 + room[0]
    human = human[1]*256 + human[0]
    room*=2
    human*=2
    if room > 27315:
        room -= 27315
    else:
        room = 27315 - room
    if human > 27315:
        human -= 27315
    else:
        human = 27315 - human
    room/=100
    human/=100
    return room,human
