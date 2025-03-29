import csv
from guitar import Guitar


def main():
    """Manage and display guitars."""

    file_name = "guitars.csv"
    guitars = read_csv(file_name)

    if guitars:
        print("Guitars:")
        for guitar in guitars:
            print(guitar)

        new_guitars = get_guitars()
        guitars.extend(new_guitars)

        guitars.sort()

        print("\nGuitars (Sorted by Year):")
        for guitar in guitars:
            print(guitar)
    else:
        print("No guitars found in the file.")


def read_csv(file_name):
    """Read guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    try:
        with open(file_name, mode="r", newline="") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                name = row[0]
                year = int(row[1])
                cost = float(row[2])
                guitars.append(Guitar(name, year, cost))
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    return guitars


def write_csv(file_name, guitars):
    """Write guitars to a CSV file."""
    try:
        with open(file_name, mode="w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Name", "Year", "Cost"])  # Write the header row
            for guitar in guitars:
                writer.writerow([guitar.name, guitar.year, guitar.cost])
    except Exception as e:
        print(f"Error writing to file: {e}")


def get_guitars():
    """Ask the user to enter new guitars and return them as a list of Guitar objects."""
    new_guitars = []
    print("Enter your new guitars:")
    name = input("Name: ").strip()
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitars.append(Guitar(name, year, cost))
        name = input("Name: ").strip()
    return new_guitars


main()
