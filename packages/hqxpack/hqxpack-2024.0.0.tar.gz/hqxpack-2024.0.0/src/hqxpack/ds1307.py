from machine import I2C, Pin
import utime
import time

i2c = I2C(0)
# HM时钟模块的I2C地址
HM_CLOCK_ADDRESS = 0x68

def int_to_bcd(n):
    return (n // 10) << 4 | (n % 10)

def bcd_to_int(bcd):
    return ((bcd & 0xF0) >> 4) * 10 + (bcd & 0x0F)

def set_time(year, month, day, hour, minute, second):
    time_data = bytearray(7)
    time_data[0] = int_to_bcd(second)
    time_data[1] = int_to_bcd(minute)
    time_data[2] = int_to_bcd(hour)
    time_data[3] = 0
    time_data[4] = int_to_bcd(day)
    time_data[5] = int_to_bcd(month)
    time_data[6] = int_to_bcd(year - 2000)
    i2c.writeto_mem(HM_CLOCK_ADDRESS, 0x00, time_data)

def get_time():
    time_data = i2c.readfrom_mem(HM_CLOCK_ADDRESS, 0x00, 7)
    second = bcd_to_int(time_data[0])
    minute = bcd_to_int(time_data[1])
    hour = bcd_to_int(time_data[2])
    day = bcd_to_int(time_data[4])
    month = bcd_to_int(time_data[5])
    year = bcd_to_int(time_data[6]) + 2000
    return (year, month, day, hour, minute, second)