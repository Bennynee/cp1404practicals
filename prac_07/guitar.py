class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """Return the age of the guitar in years."""
        current_year = 2025
        return current_year - self.year

    def __lt__(self, other):
        """Return True if the guitar is 50 or more years old."""
        return self.year < other.year

    def __str__(self):
        """Return a string representation of the Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"
