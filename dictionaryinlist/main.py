travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇
country = ""
visits = 0
cities = []


def add_new_country(country, visits, cities):
    travel_log.append(
        {"country": country,
         "visits": visits,
         "cities": cities
         }
    )
#Alternate method, easier to read
# def add_new_country(country, visits, cities):
#     newCountry = {}
#     newCountry["country"] = country
#     newCountry["visits"] = visits
#     newCountry["cities"] = cities
#     travel_log.append(newCountry)

# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
