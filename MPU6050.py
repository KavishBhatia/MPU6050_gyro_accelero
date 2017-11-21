#!/usr/bin/python

import smbus
import math
import time
import signal
import subprocess
import sys
import os

##gyro = []
##accelero = []

class MPU6050:
    try:
        def MPU6050():
            bus = 0
            high, low, value = 0
            radians = 0
            address = 0
            power_mgmt_1 = 0
            power_mgmt_2 = 0
            gyro_xout, gyro_yout, gyro_zout = 0
            accel_xout, accel_yout, accel_zout = 0
##            gyro = []
##            accelero = []
            adr = 0
            
        def init(self):
            # Power management registers
            self.power_mgmt_1 = 0x6b
            self.power_mgmt_2 = 0x6b
    
            self.bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
            self.address = 0x68       # This is the address value read via the i2cdetect command

            # Now wake the 6050 up as it starts in sleep mode
            try:
                self.bus.write_byte_data(self.address, self.power_mgmt_1, 0)
            except IOError:
                subprocess.call(['i2cdetect', '-y', '1'])
                flag = 1     #optional flag to signal your code to resend or something    
            
        def read_byte(self,adr):
            return self.bus.read_byte_data(self.address, self.adr)

        def read_word(self,adr):
            try:
                self.high = self.bus.read_byte_data(self.address, self.adr)
                self.low = self.bus.read_byte_data(self.address, self.adr+1)
                self.val = (self.high << 8) + self.low
                return self.val
            except:
                subprocess.call(['i2cdetect', '-y', '1'])
                flag = 1     #optional flag to signal your code to resend or something
                
        def read_word_2c(self, adr):
            self.adr = adr
            self.val = self.read_word(self.adr)
            if (self.val >= 0x8000):
                return -((65535 - self.val) + 1)
            else:
                return self.val

        def dist(self,a,b):
            return math.sqrt((self.a*self.a)+(self.b*self.b))

        def get_y_rotation(self,x,y,z):
            self.radians = math.atan2(self.x, dist(self.y, self.z))
            return -math.degrees(self.radians)

        def get_x_rotation(self, x, y, z):
            self.radians = math.atan2(self.y, dist(self.x, self.z))
            return math.degrees(self.radians)

        def gyro_data(self):
            self.gyro = []
            self.gyro_xout = self.read_word_2c(0x43)
            self.gyro_yout = self.read_word_2c(0x45)
            self.gyro_zout = self.read_word_2c(0x47)
            self.gyro.append(self.gyro_xout)
            self.gyro.append(self.gyro_yout)
            self.gyro.append(self.gyro_zout)
            return self.gyro
        
        def accelerometer_data(self):
            self.accelero = []
            self.accel_xout = self.read_word_2c(0x3b)
            self.accel_yout = self.read_word_2c(0x3d)
            self.accel_zout = self.read_word_2c(0x3f)
            self.accelero.append(self.accel_xout)
            self.accelero.append(self.accel_yout)
            self.accelero.append(self.accel_zout)
            return self.accelero
        
    except KeyboardInterrupt:
        print 'Interrupted'
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
        finally:
            sys.exit(0)
