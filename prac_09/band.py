class Band:
    """Band class to represent a band that has musicians."""

    def __init__(self, name):
        """Construct a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band."""
        musicians_str = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_str})"

    def __repr__(self):
        """Return a string representation showing the variables."""
        return str(vars(self))

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string describing what each musician is playing."""
        return "\n".join(musician.play() for musician in self.musicians)