import RPi.GPIO as GPIO
import time
import MPU6050

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

while True:
    #making object of class MPU6050
    mpu = MPU6050.MPU6050()
    
    #calling initializing function
    mpu.init()

    #get gyro data
    gyro = mpu.gyro_data()

    #get accelerometer data
    accel = mpu.accelerometer_data()

    #print acquired data
    print "gyro(x, y, z) - ", gyro
    print "accelerometer(x, y, z) - ", accel

    time.sleep(1)
