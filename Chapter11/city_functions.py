def FormatCountryCity(countryName, cityName, population = "-1"):
    
    if population == "-1":
        return f"{cityName}, {countryName}"
    else:
        return f"{cityName}, {countryName} - Population: {population}"

FormatCountryCity("Russia", "Volgograd", "1019000")