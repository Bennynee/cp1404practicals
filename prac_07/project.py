from datetime import datetime


class Project:
    """Represent a project with details like name, start date, priority, cost, and completion."""

    def __init__(self, name, start_date, priority, cost_estimate, completion):
        """Initialize a Project instance."""
        self.name = name
        if isinstance(start_date, str):
            self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        else:
            self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion = int(completion)

    def is_complete(self):
        """Check if the project is completed."""
        return self.completion == 100

    def update(self, new_completion=None, new_priority=None):
        """Update the project's completion and priority."""
        if new_completion is not None:
            self.completion = int(new_completion)
        if new_priority is not None:
            self.priority = int(new_priority)

    def __lt__(self, other):
        """Compare projects by priority for sorting."""
        return self.priority < other.priority

    def __str__(self):
        """Return a string representation of the Project."""
        start_date_str = self.start_date.strftime("%d/%m/%Y")
        return (f"{self.name}, start: {start_date_str}, priority: {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion}%")
