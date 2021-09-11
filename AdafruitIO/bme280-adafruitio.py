# Output to log file has been disabled while testing with adafruit io
# This script uses a BME280 sensor. If you want a script that uses bot the bme280 and mcp9808 please see that script.

import time
import board
from adafruit_bme280 import basic as adafruit_bme280
import adafruit_mcp9808
from Adafruit_IO import Client, Feed


# Set sample rate
sample_rate = 5

# AdafruitIO user data
ADAFRUIT_IO_KEY = 'input api key here using nano on host raspi'
ADAFRUIT_IO_USERNAME = 'input username here using nano on host raspi'

# Create instance of the REST client
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Set up Adafruit IO Feeds, name these according to what you will be naming your feeds for this specific project in adafruitIO
temperature_feed = aio.feeds('breadboard-temp')
humidity_feed = aio.feeds('breadboard-humidity')
pressure_feed = aio.feeds('breadboard-pressure')

# Create sensor object, using the board's default I2C bus.
i2c = board.I2C()  # uses board.SCL and board.SDA
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)


# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1010.00



while True:
    # Create variables for temp, humidity, and pressure (bme280)
    temp = bme280.temperature * 9/5 + 32
    humidity = bme280.relative_humidity
    pressure = bme280.pressure
    #altitude = bme280.altitude * 3.28084


    # Print values to terminal
    print("\nbmeTemp: %0.2f F" % temp)
    print("Humidity: %0.2f %%" % humidity)
    print("Pressure: %0.2f hPa" % pressure)
    #print("Altitude = %0.2f feet" % altitude)


    if humidity is not None and temp is not None:

        # Send humidity and temperature feeds to Adafruit IO
        temp = '%.2f F'%(temp)
        humidity = '%.2f %%'%(humidity)
        pressure = '%.2f hPa'%(pressure)
        aio.send(temperature_feed.key, str(temp))
        aio.send(humidity_feed.key, str(humidity))
        aio.send(pressure_feed.key, str(pressure))

    else:
        print('Failed to get Reading, trying again in ', sample_rate, 'seconds')
    # Timeout to avoid flooding Adafruit IO

    time.sleep(sample_rate)
