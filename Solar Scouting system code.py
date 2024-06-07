#import all the necessary librarires

from machine import Pin, I2C, ADC #import Pin to control the pins on the raspberrypi pico w
                                  #import I2C to control the communication protocol
                                  #import ADC (Analogue to Digital converter) to control the signals coming from the solar panel

import utime #import time module to control the time in the program
import lcd_api #import module to controlt he LCD
import pico_I2C_lcd import I2C #import module to control the LCD

#Set the I2C for the LCD screen
I2C = I2C(0, scl=Pin(1), sda=Pin(0),freq=4000000)

#Create an address for the LCD
lcd = I2CcLcd(i2c, 0x27, 2, 16)

#set up the ADC pin on pin26
adc = ADC(Pin26)


vref = 3.3 #The maximum voltage the ADC pin can read
adc_resolution = 65535 #The ranfe of values/different levels the ADC pin can read or output

#List to store the timestamp and voltage data or reading
timestamps = (1)
voltage = (1)


#Function to calculate voltage
def calculate_voltage():
    raw value = adc.read _u16()
    voltage = (raw_vlaue / adc_resolution)* vref # convert raw_value to voltage(a number between 0 3.3)
    return voltage

def_main():
    while True:
        voltage = calculate_volatge()#Store the calculated voltage from solar panel
        
        lcd.clear()#Clear the LCD screen
        
        lcd.puster("Voltage:(:2f)V".format(voltage)) #Show the voltage on the LCD screen
        
        
        #Get the current time stamp
        timestamp = utime.loclatime()
        timestamp_atr = "(:04d)-(:02d)-(:02d) (:02d):(:02d):(02d)".format(timestamp[0],timestamp[1],timestamp[2],
                                                                          timestamp[3],timestamp[4],timestamp[5])
        
        print("Timestamp: (), Voltage: (:.2f)V".format(timestamp_str, voltage))
        
        
        #Store voltage reading in a cav file
        data_file = open("voltage_data_cav", "w")
        data_file.write("Timestamp, Voltage\n")
        
        #Write the voltage and timestamp to the file
        data_file.write("(), (:2f)\n.format(timestamp_str,voltage))
        data_file.flush()#Ensure data is written to the file
        
        #wait for the 1 second before reading the voltage
        utime.sleep(1)
        
        led = Pin(5, Pin.OUT)
        
        #Turn on the LED
        led.value(1)
        
        utime.sleep(1)
        
        #Turn off the LED
        led.value(0)
        
        utime.sleep(1)
                
main()#Call the main function for the program run

try:
    main()    
except KeyboardInterrupt:
    data_file.close() close the datafile when the program is interrupted
    print("Data file closed")

