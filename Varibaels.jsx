class ConstructionProject {
    constructor(name, location, budget, startDate, endDate) {
        this.name = name;
        this.location = location;
        this.budget = budget;
        this.startDate = new Date(startDate);
        this.endDate = new Date(endDate);
        this.tasks = [];
        this.completed = false;
    }

    addTask(taskName, assignedTo, dueDate) {
        this.tasks.push({
            taskName,
            assignedTo,
            dueDate: new Date(dueDate),
            completed: false
        });
    }

    completeTask(taskName) {
        const task = this.tasks.find(t => t.taskName === taskName);
        if (task) {
            task.completed = true;
        }
    }

    getProgress() {
        if (this.tasks.length === 0) return 0;
        const completedTasks = this.tasks.filter(t => t.completed).length;
        return (completedTasks / this.tasks.length) * 100;
    }

    markCompleted() {
        this.completed = true;
    }

    getSummary() {
        return {
            name: this.name,
            location: this.location,
            budget: this.budget,
            startDate: this.startDate,
            endDate: this.endDate,
            totalTasks: this.tasks.length,
            progress: this.getProgress(),
            completed: this.completed
        };
    }
}

// Example usage:
const project = new ConstructionProject(
    "Library Renovation",
    "123 Main St",
    500000,
    "2024-07-01",
    "2025-01-31"
);

project.addTask("Demolition", "Team A", "2024-07-15");
project.addTask("Foundation", "Team B", "2024-08-01");
project.completeTask("Demolition");

console.log(project.getSummary());  <console className="log"></console>

console.error(encodeURIComponent()); postMessage; (RTCDataChannel) ='error' 
console.log("project", project); return project.getSummary(); 


// I removed  />resizeTo={ which caused sime issues with syntax..

// Example of valid usage:
addEventListener("message", (event) => {
    console.log("Received message:", event.data);
});

matchMedia("(max-width: 600px)");

/* If you want to use asserts, provide a valid assertion function or remove it if not needed */
// asserts(true); // Uncomment and define asserts if needed
 

queueMicrotask(encodeURIComponent);