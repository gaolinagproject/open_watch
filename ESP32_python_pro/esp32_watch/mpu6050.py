

from machine import Pin,I2C
import time



SMPLRT_DIV		= const(0x19) #陀螺仪采样率，典型值：0x07(125Hz)
CONFIG			  = const(0x1A) #//低通滤波频率，典型值：0x06(5Hz)
GYRO_CONFIG		= const(0x1B) #//陀螺仪自检及测量范围，典型值：0x18(不自检，2000deg/s)
ACCEL_CONFIG	= const(0x1C) #//加速计自检、测量范围及高通滤波频率，典型值：0x01(不自检，2G，5Hz)
ACCEL_XOUT_H	= const(0x3B) #
ACCEL_XOUT_L	= const(0x3C) #
ACCEL_YOUT_H	= const(0x3D) #
ACCEL_YOUT_L	= const(0x3E) #
ACCEL_ZOUT_H	= const(0x3F) #
ACCEL_ZOUT_L	= const(0x40) #
TEMP_OUT_H		= const(0x41) #
TEMP_OUT_L		= const(0x42) #
GYRO_XOUT_H		= const(0x43) #
GYRO_XOUT_L		= const(0x44) #	
GYRO_YOUT_H		= const(0x45) #
GYRO_YOUT_L		= const(0x46) #


GYRO_ZOUT_H		= const(0x47) #


GYRO_ZOUT_L		= const(0x48) #


PWR_MGMT_1		= const(0x6B) #	//电源管理，典型值：0x00(正常启用)


WHO_AM_I			= const(0x75) #	//IIC地址寄存器(默认数值0x68，只读)


SlaveAddress	= const(0xD0) #	//IIC写入时的地址字节数据，+1为读取

class mpu6050(object):
    def __init__(self):
      self.i2c = I2C(-1,scl=Pin(17), sda=Pin(16),freq=400000)
      self.i2c_address = self.i2c.scan()[0]
      print("mpu6050_add = ",self.i2c_address)
      self.mpu6050_write_reg(PWR_MGMT_1,0x00)
      self.mpu6050_write_reg(SMPLRT_DIV,0x07)
      self.mpu6050_write_reg(CONFIG,0x06)
      self.mpu6050_write_reg(GYRO_CONFIG,0x18)
      self.mpu6050_write_reg(ACCEL_CONFIG,0x01)
      
    def mpu6050_write_reg(self,uch_addr,uch_data):
     # buf = bytearray(1)
      #buf[0] = uch_data
      self.i2c.writeto_mem(self.i2c_address, uch_addr , chr(uch_data))
      #self.i2c.writeto(uch_addr, buf)
      
    def mpu6050_read_reg(self,uch_addr):
      buf = self.i2c.readfrom_mem(self.i2c_address, uch_addr , 1)
      return buf
     
    def git_data(self,uch_addr):
      h_adta = self.mpu6050_read_reg(uch_addr)
      l_adta = self.mpu6050_read_reg(uch_addr + 1)
      return (ord(h_adta) << 8) + ord(l_adta)

      
    def mpu6050_data(self):
      t = []
      t.append(self.git_data(ACCEL_XOUT_H))
      t.append(self.git_data(ACCEL_YOUT_H))
      t.append(self.git_data(ACCEL_ZOUT_H))
      t.append(self.git_data(GYRO_XOUT_H))
      t.append(self.git_data(GYRO_YOUT_H))
      t.append(self.git_data(GYRO_ZOUT_H))
      return t

