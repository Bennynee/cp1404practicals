from prac_09.silver_service_taxi import SilverServiceTaxi

# Create a SilverServiceTaxi object
fancy_taxi = SilverServiceTaxi("Hummer", 200, 2)

# Drive the taxi 18 km
fancy_taxi.drive(18)

# Assert tests
assert fancy_taxi.get_fare() == 48.78, "Fare calculation is incorrect!"

# Print the taxi's details and the fare
print(fancy_taxi)
print(f"Fare: ${fancy_taxi.get_fare():.2f}")