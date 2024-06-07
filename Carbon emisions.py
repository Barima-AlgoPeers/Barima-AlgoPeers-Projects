# ALGOPEERS TEST 3 (REAL WORK)

# CODES
# VARIABLES
distance = 10000 # The variable distance holds 10,000 kilometers
gasoline_cars_emition = 0.24 # The variable gasoline cars emition holds 0.24kg of C02
electric_cars_emition = 0.05 # The variable electric cars emition holds 0.05kg of C02

# CARBON EMITION CALCULATION
gasoline_cars_total_emition_distance = gasoline_cars_emition * distance # This would calculate the total emition for the gasoline cars in 10,000 km
electric_cars_total_emition_distance = electric_cars_emition * distance # This would calculate the total emition for the electric cars in 10,000 km

# PRINTING EMISIONS
print(f'Emissions for a gasoline car over {distance} km: {gasoline_cars_total_emition_distance:.0f} kg') # Print the answer
print(f'Emissions for an electric car over {distance} km: {electric_cars_total_emition_distance:.0f} kg') # Print the answer