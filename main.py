import time
import board
import adafruit_bmp3xx
import adafruit_mpu6050

# i2c connection for mpu 6050
i2c = board.I2C()
mpu = adafruit_mpu6050.MPU6050(i2c)

# bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c)

# SPI setup

from digitalio import DigitalInOut, Direction
#import RPi.GPIO as GPIO
import board
spi = board.SPI()
cs = DigitalInOut(board.D5)
bmp = adafruit_bmp3xx.BMP3XX_SPI(spi, cs)

bmp.pressure_oversampling = 8 #for bmp390
bmp.temperature_oversampling = 2

while True:
    print(
        "Pressure: {:6.4f} hPa Temperature: {:5.2f} C Altitude: {:5.4f} m".format(bmp.pressure, bmp.temperature, bmp.altitude)
    )
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu.acceleration))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f rad/s" % (mpu.gyro))
    print("Gyro Temperature: %.2f C" % mpu.temperature)
    print("")
    time.sleep(1)
