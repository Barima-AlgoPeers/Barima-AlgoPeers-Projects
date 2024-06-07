#                                                           ALGO PEERS TEST 2
#                                                              VARIABLES
temp1 = '72.5'
print(temp1)

temp2 = '75.0'
print(temp2)

temp3 = '68.5'
print(temp3)

temp4 = '70.0'
print(temp4)

temp5 = '71.5'
print(temp5)

temp6 = '69.0'
print(temp6)

temp7 = '74.0'
print(temp7)

#                                                CONVERTION OF STRINGS TO FLOATS
temperatures = [float(temp1), float(temp2),float(temp3), float(temp4), float(temp5), float(temp6), float(temp7)]


#                                                          AVERAGE CHANGING
average = sum(temperatures) / len(temperatures)


#                                                          PRINTING AVERAGE
print(f"Average Temperature: {average:.1f} Farenhiet")