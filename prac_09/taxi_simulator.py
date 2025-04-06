from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulator program."""
    print("Let's drive!")
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4),
    ]
    bill = 0.0
    current_taxi = None

    while True:
        print(MENU)
        choice = input(">>> ").lower()

        if choice == "q":
            break
        elif choice == "c":
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            if current_taxi:
                bill += drive_taxi(current_taxi)
            else:
                print("You need to choose a taxi before you can drive.")
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill:.2f}")

    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    list_taxis(taxis)


def choose_taxi(taxis):
    """Let the user choose a taxi from the list."""
    print("Taxis available:")
    list_taxis(taxis)
    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid input; please enter a number.")
    return None


def drive_taxi(taxi):
    """Drive the chosen taxi and return the trip cost."""
    try:
        distance = float(input("Drive how far? "))
        distance_driven = taxi.drive(distance)
        trip_cost = taxi.get_fare()
        print(f"Your {taxi.name} trip cost you ${trip_cost:.2f}")
        taxi.start_fare()
        return trip_cost
    except ValueError:
        print("Invalid input; please enter a number.")
        return 0.0


def list_taxis(taxis):
    """Display a list of all taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == "__main__":
    main()