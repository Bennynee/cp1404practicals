import csv
from datetime import datetime
from project import Project

MENU = ("\n- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n"
        "- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit")


def main():
    """Main menu for the project management program."""
    projects = load_projects("projects.txt")
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from projects.txt.")
    print(MENU)
    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "l":
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Filename: ")
            save_projects(filename, projects)
            print(f"Projects saved to {filename}.")
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_project(projects)
        elif choice == "u":
            update_project(projects)
        else:
            print("Invalid option. Please try again.")
        print(MENU)
        choice = input(">>> ").lower()

    if input("Would you like to save to projects.txt? (Y/N): ").lower() == "y":
        save_projects("projects.txt", projects)
    print("Thank you for using the project management software!")


def load_projects(filename):
    """Load projects from a file."""
    projects = []
    try:
        with open(filename, mode="r", newline="") as file:
            reader = csv.reader(file, delimiter="\t")
            next(reader)
            for row in reader:
                projects.append(Project(*row))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return projects


def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file, delimiter="\t")
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion"])
        for project in projects:
            writer.writerow([
                project.name,
                project.start_date.strftime("%d/%m/%Y"),
                project.priority,
                project.cost_estimate,
                project.completion
            ])


def get_priority(project):
    """Return the priority of a project for sorting."""
    return project.priority


def display_projects(projects):
    """Display incomplete and completed projects, sorted by priority."""
    incomplete = sorted([p for p in projects if not p.is_complete()], key=get_priority)
    complete = sorted([p for p in projects if p.is_complete()], key=get_priority)

    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")
    print("Completed projects:")
    for project in complete:
        print(f"  {project}")


def get_start_date(project):
    """Return the start date of a project for sorting."""
    return project.start_date


def filter_projects_by_date(projects):
    """Filter projects by start date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()

        filtered_projects = [p for p in projects if p.start_date >= filter_date]
        filtered_projects.sort(key=get_start_date)

        for project in filtered_projects:
            print(f"  {project}")
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")


def add_project(projects):
    """Add a new project."""
    try:
        name = input("Project name: ")
        start_date = datetime.strptime(input("Start date (dd/mm/yyyy): "), "%d/%m/%Y").date()
        priority = int(input("Priority: "))
        cost_estimate = float(input("Cost estimate: $"))
        completion = int(input("Percent complete: "))
        projects.append(Project(name, start_date, priority, cost_estimate, completion))
    except ValueError:
        print("Invalid input. Please try again.")


def update_project(projects):
    """Update a project's completion and/or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        project_index = int(input("Project choice: "))
        project = projects[project_index]
        print(project)

        new_completion = input("New Percentage: ")
        new_priority = input("New Priority: ")

        if new_completion:
            project.completion = int(new_completion)
        if new_priority:
            project.priority = int(new_priority)
    except (ValueError, IndexError):
        print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
