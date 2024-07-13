from machine import Pin,ADC
import onewire, ds18x20
import time

# 初始化温度、光线、磁力传感器
def temp(num):
    if 'int' not in str(type(num)) :
        print('参数有误')
        return 
    ds1820 = ds18x20.DS18X20(onewire.OneWire(Pin(num)))
    rom = ds1820.scan()
    ds1820.convert_temp() 
    temp = ds1820.read_temp(rom[0])
    return temp
