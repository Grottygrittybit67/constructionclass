class Construction:
    def __init__(self, name):
        self.name = name

    def print_text(self):
        print(f"Construction project: {self.name}")

if __name__ == "__main__":
    project = Construction("Bridge Renovation")
    project.print_text()

Construction("Bridge Renovation").print_text()

help(Construction) #this will explain the class and its methods 

print(Construction.__doc__) # open (globals) 

project = Construction("Bridge Renovation")      