# Dictionary

capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
}

# Nested list in Dictionary

travel_log = {
    "France" : ["Paris", "Lille", "Dij" ],
    "Germany" : ["Stuttgart", "Berlin"],
}

print(travel_log["France"][1])

# Nested list
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

# List in Dictionary in Dictionary
travel_log2 = {
    "France" : {
        "cities_visited" : ["Paris", "Lille", "Dij"],
        "total_visits" : 12,
    },
    "Germany" : {
        "cities_visited" : ["Berlin", "Hamburg","Stuttgart"],
        "total_visits" : 5,
},
}
print(travel_log2["Germany"]["cities_visited"][2])
