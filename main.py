import time
import adafruit_bmp3xx

# i2c = board.I2C()
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
    time.sleep(1)
