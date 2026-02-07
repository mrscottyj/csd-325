def get_city_country(city, country, population='', language=''):
    """Generate a neatly formatted city, country string with optional population and language."""
    if population and language:
        city_country = f"{city}, {country} - population {population}, {language}"
    elif population:
        city_country = f"{city}, {country} - population {population}"
    elif language:
        city_country = f"{city}, {country}, {language}"
    else:
        city_country = f"{city}, {country}"
    return city_country.title()


# Call the function three times with different city/country values
print(get_city_country('santiago', 'chile', 5000000, 'spanish'))
print(get_city_country('cologne', 'germany', 1085000, 'german'))
print(get_city_country('rotterdam', 'netherlands', 651000, 'dutch'))