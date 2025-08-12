class Construction:
    def __init__(self, name, worker="Theon"):
        self.name = name
        self.worker = worker
        self.status = "Planning"
        self.budget = 0
        self.materials = []
        self.timeline = {
            "start_date": None,
            "end_date": None
        }
    
    def set_budget(self, amount):
        self.budget = amount
        print(f"Budget set to ${amount:,.2f}")
    
    def add_material(self, material, quantity):
        self.materials.append({"material": material, "quantity": quantity})
        print(f"Added {quantity} units of {material}")
    
    def update_status(self, new_status):
        self.status = new_status
        print(f"Project status updated to: {new_status}")
    
    def set_timeline(self, start_date, end_date):
        self.timeline["start_date"] = start_date
        self.timeline["end_date"] = end_date
        print(f"Timeline set: {start_date} to {end_date}")
    
    def project_summary(self):
        print(f"\nProject Summary for: {self.name}")
        print(f"Worker in charge: {self.worker}")
        print(f"Current Status: {self.status}")
        print(f"Budget: ${self.budget:,.2f}")
        print("\nMaterials:")
        for item in self.materials:
            print(f"- {item['quantity']} units of {item['material']}")
        print(f"\nTimeline: {self.timeline['start_date']} to {self.timeline['end_date']}")

# Example usage
if __name__ == "__main__":
    # Create a new construction project
    project = Construction("Bridge Renovation")
    
    # Set project details
    project.set_budget(500000)
    project.add_material("Steel Beams", 50)
    project.add_material("Concrete", 200)
    project.set_timeline("2025-08-10", "2026-02-10")
    project.update_status("In Progress")
    
    # Print project summary
    project.project_summary()
