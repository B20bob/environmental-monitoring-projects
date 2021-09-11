# Run with Python3.
# This script was written for use with raspberry pi.
# BME280 & MCP9808 are connected using i2c and their default addresses. These adresses can be changed in the respective lines below if needed.
# It is required to have Circuitpython & Blinka installed and working to run this script, please see README for links to Adafruit guide.
# Please see README for guides and sources to install required libraries and hardware.

# This script collects tempurature, humidity, and barometric pressure data using a combination of BME280 and MCP9808 sensors. It outputs that data to the terminal,
# as well as logs it to a .csv file. This .csv file can be opened with any spreadsheet software and used to create charts and graphs if desired.


import time
import board
from adafruit_bme280 import basic as adafruit_bme280
import adafruit_mcp9808

# Create sensor object, using the board's default I2C bus.
i2c = board.I2C()  # uses board.SCL and board.SDA
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)

# To initialise using a specified address:
# Necessary when, for example, connecting A0 to VDD to make address=0x19
mcp = adafruit_mcp9808.MCP9808(i2c, address=0x18)

# OR create sensor object, using the board's default SPI bus.
# spi = board.SPI()
# bme_cs = digitalio.DigitalInOut(board.D10)
# bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, bme_cs)

# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1010.00

file = open("bme280-log.csv", "w")
file.write("Time and Date, Temperature, Humidity, Pressure\n")


while True:
    # Create variables for temp, humidity, and pressure (bme280)
    temp = bme280.temperature * 9/5 + 32
    humidity = bme280.relative_humidity
    pressure = bme280.pressure
    altitude = bme280.altitude * 3.28084

   # Create variables for temp (mcp9808)
    mcpTemp = mcp.temperature * 9/5 + 32

#    Round variables to 2 decimal places, and create new variables to use in log print string below
    mcpTempR = round(mcpTemp, 2)
    bmetempR = round(temp, 2)
    humidityR = round(humidity,2)
    pressureR = round(pressure, 2)
    # altitudeR = round(altitude, 2)

    # Print values to terminal
    print("\nmcpTemp: %0.2f F" % mcpTemp)
    print("bmeTemp: %0.2f F" % temp)
    print("Humidity: %0.2f %%" % humidity)
    print("Pressure: %0.2f hPa" % pressure)
    #print("Altitude = %0.2f feet" % altitude)

    # Open log file and write data to it
    file.write(time.strftime("%H:%M:%S %d/%m/%Y") + ', ' + str(bmetempR) + "," + str(humidityR) + "," + str(pressureR) + "," + str(mcpTempR) + "\n")
    
    # Set sample rate here (in seconds)
    time.sleep(300)