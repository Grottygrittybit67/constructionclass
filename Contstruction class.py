
class Construction:
    def __init__(self, name, location=None, budget=0.0):
        self.name = name
        self.location = location
        self.budget = budget
        self.status = "Not Started"

    def print_text(self):
        print(f"Construction project: {self.name}")

    def start_project(self):
        self.status = "In Progress"
        print(f"Project '{self.name}' has started.")

    def complete_project(self):
        self.status = "Completed"
        print(f"Project '{self.name}' is completed.")

    def update_budget(self, new_budget):
        self.budget = new_budget
        print(f"Budget for '{self.name}' updated to ${self.budget:,.2f}.")

    def get_summary(self):
        return (
            f"Project: {self.name}\n"
            f"Location: {self.location}\n"
            f"Budget: ${self.budget:,.2f}\n"
            f"Status: {self.status}"
        )


if __name__ == "__main__":
    project = Construction("Bridge Renovation", location="Downtown", budget=5000000)
    project.print_text()
    project.start_project()
    project.update_budget(5500000)
    print(project.get_summary())
    project.complete_project()
    print(project.get_summary())

    # Old usage for compatibility
    Construction("Bridge Renovation").print_text()

    help(Construction)  # this will explain the class and its methods
    print(Construction.__doc__)
