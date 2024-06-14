# ALGO PEERS PROJECTS

# SOLAR SCOUTING SYSTEM PROJECT

# CODES:

# Import all necessary libaries:
from machine import Pin, I2C, ADC # Import Pin  module to control the pins on the raspberry Pi Pico W.
                                  # Import I2C to control the communication protocol.
                                  # Import ADC (Analog to Digital Converter) to contol the signals coming to the solar panel.
                                  
import utime # Import time module to control the time in the program.
import lcd_api # Import module to control the LCD.
from pico_i2c_lcd import I2cLcd # Import module to control the LCD.


# Setting up of pins:
# Set the I2C for the LCD screen.
i2c = I2C(0, scl=Pin(1) , sda=Pin(0), freq=4000000)


# Create an address for the LCD:
lcd = I2cLcd(i2c, 0x27, 2, 16)

# Set up the ADC pin on pin 26:
adc = ADC(Pin(26))


# Voltage:
vref = 3.3 # The maximum votage the ADC pin can read.
adc_resolution = 65535 # The range of values/different levels the ADC pin can read or output.


# Lists:
timestamps = [] # List storing timestamps.
voltage = [] # List storing voltages.

# Function to calculate voltge:
def calculate_voltage():
    raw_value = adc.read_u16() # Get raw value from ADC (a number between 0, 65, and 535)
    voltage = (raw_value / adc_resolution)* vref # Convert raw_value to voltage (a number betwween 0 and 3.3)
    return voltage

def append_data_to_file(timestamp_str,voltage):
    try:
        with open("voltage_data.csv", "a") as data_file: # Open the file in append mode.
            data_file.write("{}. (:.2f\n".format(timestamp_str, voltage))
    except Exception as e:
        print("Error writing to the file:" e)
    
def main():
    while True:
        voltage = calculate_voltage() # Store the calculated voltage from solar panel.
        
        lcd.clear() # Clear the LCD screen
        
        lcd.putstr("Voltage: {:2f}V".format(voltage)) # Show the voltage on the LCD screen.
        
        
        # Get the current timestamp
        timestamp = utime.localtime()
        timestamp_str = "{:O4d}-{:02d}-{:O2d} {:O2d}:{:O2d}:{:O2d}".format(timestamp[0], timestamp[1], timestamp[2], timestamp[3], timestamp[4], timestamp[5])
        
        
        print("Timestamp: {}, Voltage: {:2f}V".format(timestamp_str, voltage))
        
        
        # Store voltage reading in a csv file:
        data_file = open("voltage_data_csv", "w")
        data_file.write("Timestamp, Voltage\n")
        
        # Write the voltage and timestamp to the file
        data_file.write("{}, {:2f}\n".format(timestamp_str, voltage))
        data_file.flush() # Ensure data is written to the file
        
        append_data_to_file(timestamp_str, voltage)
        
        # Wait for the 1 second before reading the voltage
        utime.sleep(1)
        
        led = Pin(5, Pin.OUT)
        
        # Turn on the LED
        led.value(1)
        
        utime.sleep(1)
        
        # Turn off the LED
        led.value(0)
        
        utime.sleep(1)
         
try:
    main()
except KeyboardInterrupt:
    print ("Program Interrupted")

try:
    with open("voltage_data.csv", "r") as data_file:
        pass
except OSError:
    with open("voltage_data.csv", "w") as data_file:
        data_file.write("Timestamp, Voltage\n")
