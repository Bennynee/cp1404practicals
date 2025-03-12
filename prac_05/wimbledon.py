FILE_NAME = "wimbledon.csv"


def main():
    data = read_file(FILE_NAME)

    champions = get_champions(data)
    print("Wimbledon Champions:")
    for champion, wins in champions.items():
        print(f"{champion} {wins}")

    countries = get_countries(data)
    countries_string = ', '.join(countries)
    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(countries_string)


def read_file(filename):
    """Read the CSV file and return the data as a list of lists."""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as file:
        next(file)
        for line in file:
            parts = line.strip().split(',')
            data.append(parts)
    return data


def get_champions(data):
    """Process the data to count the number of wins for each champion."""
    champions = {}
    for row in data:
        champion = row[2]
        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1
    return champions


def get_countries(data):
    """Get a sorted set of countries of the champions."""
    countries = set()
    for row in data:
        country = row[1]
        countries.add(country)
    return sorted(countries)


main()
