# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

def greet_with_data(name, location):
    print(f"Hello {name}, your location is {location}")

greet_with_data("Dinda", "Depok")
greet_with_data(location = "Depok", name = "Dinda")
