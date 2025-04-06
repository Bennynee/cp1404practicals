from prac_09.unreliable_car import UnreliableCar

unreliable_car = UnreliableCar("DodgyCar", 50, 60)


print(unreliable_car)
for i in range(5):
    distance_driven = unreliable_car.drive(10)
    print(f"Attempt {i + 1}: Tried to drive 10 km, actually drove {distance_driven} km")
    print(unreliable_car)