# ALGOPEERS TEST 2
# ( CAR EMISSIONS )

# CODES
# VARIABLES
low_emissions_text = "Low"
moderate_emissions_text = "Moderate, reduce it a bit"
high_emissions_text = "High, very bad, reduce the pollution"
very_high_emissions_text = "very high, your are going to destroy the world"

# IF AND ELSE CONDITIONAL STATEMENTS

def categories(emissions):
    if emissions <= 100:
        return low_emissions_text # When the pollution is below 100 grams, say Low
    
    
    elif emissions <= 150:
        return moderate_emissions_text  #  When the pollution is below 150 grams, say Moderate, reduce it a bit
    

    elif emissions <= 200:
        return high_emissions_text #  When the pollution is below 200 grams, say High, very bad, reduce the pollution
    
    else :
        return very_high_emissions_text  # When the pollution is too high, say very high, your are going to destroy the world
    
print(categories(180))