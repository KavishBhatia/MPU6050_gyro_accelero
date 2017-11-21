import RPi.GPIO as GPIO
import time
import MPU6050

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

while True:
    mpu = MPU6050.MPU6050()
    mpu.init()
    gyro = mpu.gyro_data()
    accel = mpu.accelerometer_data()
    print "gyro(x, y, z) - ", gyro
    print "accelerometer(x, y, z) - ", accel
    time.sleep(1)
