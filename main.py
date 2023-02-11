import time
import board
import adafruit_bmp3xx
import adafruit_mpu6050

# i2c connection for mpu 6050
#i2c = board.I2C()
#mpu = adafruit_mpu6050.MPU6050(i2c)

# bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c)

# SPI setup

from digitalio import DigitalInOut, Direction
#import RPi.GPIO as GPIO
import board
spi = board.SPI()
cs = DigitalInOut(board.D5)
bmp = adafruit_bmp3xx.BMP3XX_SPI(spi, cs)

bmp.reset()
bmp.pressure_oversampling = 8 #for bmp390
bmp.temperature_oversampling = 2
time.sleep(2)
sea_level_feet = round(bmp.altitude * 3.28084, 2)

while True:
    height_feet = bmp.altitude * 3.28084 - sea_level_feet
    print(
        "Pressure: {:6.4f} hPa Temperature: {:5.2f} C Altitude: {:5.4f} feet".format(bmp.pressure, bmp.temperature, height_feet)
    )
    #print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu.acceleration))
    #print("Gyro X:%.2f, Y: %.2f, Z: %.2f rad/s" % (mpu.gyro))
    #print("Gyro Temperature: %.2f C" % mpu.temperature)
    print("")
    time.sleep(1)
    if height_feet < 5: #if less than 5 feet
        print("Rocket Near Land !!")
