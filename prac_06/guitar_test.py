from guitar import Guitar


def main():
    """Test code to show how the Guitar class methods work as expected."""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 5000.00)

    expected_age_gibson = 103
    expected_age_another_guitar = 12
    expected_vintage_gibson = True
    expected_vintage_another_guitar = False

    print(f"{gibson.name} get_age() - Expected {expected_age_gibson}. Got {gibson.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected {expected_age_another_guitar}. Got {another_guitar.get_age()}")

    print(f"{gibson.name} is_vintage() - Expected {expected_vintage_gibson}. Got {gibson.is_vintage()}")
    print(
        f"{another_guitar.name} is_vintage() - Expected {expected_vintage_another_guitar}. "
        f"Got {another_guitar.is_vintage()}")


main()