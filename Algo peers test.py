# Question 1
# WRITE A FUNCTION TO CALCUATE THE VOLTAGE READINGS FROM A SOLAR PANEL.
vref = 3.3
adc_resolution = 65535
raw_value = 73.2
 
def voltage_function():
    voltage = (raw_value/adc_resolution) * vref
    return voltage

volts = voltage_function()
print (f"Voltage:{volts:.2f}")

# Question 2
first = 0.03
second = 8.10
third = 9.997
fourth = 1010.1
fifth = 0.003


def voltage_function2():
    float_changer1 = (first/adc_resolution) * vref
    float_changer2 = (second/adc_resolution) * vref
    float_changer3 = (third/adc_resolution) * vref
    float_changer4 = (fourth/adc_resolution) * vref
    float_changer5 = (fifth/adc_resolution) * vref
    print (f"Values:{float_changer1:.2f}")
    print (f"Values:{float_changer2:.2f}")
    print (f"Values:{float_changer3:.2f}")
    print (f"Values:{float_changer4:.2f}")
    print (f"Values:{float_changer5:.2f}")
    
    return float_changer1, float_changer2, float_changer3, float_changer4, float_changer5

volts_float = voltage_function2()
