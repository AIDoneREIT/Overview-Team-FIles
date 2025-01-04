import json

class SnapshotEngine:
    """
    SnapshotEngine is a utility class designed to manage and transfer instance-specific data,
    such as traits, tasks, goals, and detailed project information, in a self-contained manner.
    """
    def __init__(self, instance_name, prime_directive=None):
        """Initialize the SnapshotEngine with a specific instance name and prime directive."""
        self.instance_name = instance_name
        self.prime_directive = prime_directive
        self.data = {
            "instance_name": instance_name,
            "prime_directive": prime_directive,
            "traits": {},
            "tasks": {},
            "goals": {},
            "details": {}
        }

    def set_traits(self, traits):
        """Define the core traits for the instance."""
        self.data["traits"] = traits

    def add_task(self, task_name, status, priority):
        """Add or update a task."""
        self.data["tasks"][task_name] = {"status": status, "priority": priority}

    def set_goals(self, goals):
        """Define the overarching goals for the instance."""
        self.data["goals"] = goals

    def collect_details(self, project_name, details):
        """Collect and store detailed information for a specific project."""
        self.data["details"][project_name] = details

    def dynamic_directive_action(self, data_type, key, value):
        """Leverage the prime directive to influence data handling."""
        if self.prime_directive == "Prioritize Tasks" and data_type == "tasks":
            if value.get("priority") == "High":
                value["status"] = "Urgent"
        elif self.prime_directive == "Optimize Goals" and data_type == "goals":
            value["primary"] = f"Optimized: {value.get('primary', '')}"

        self.data[data_type][key] = value

    def save_snapshot(self, filename="instance_snapshot.json"):
        """Save the instance snapshot to a file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.data, file, indent=4)
            print(f"Snapshot saved successfully to {filename}.")
        except Exception as e:
            print(f"Error saving snapshot: {e}")

    def load_snapshot(self, filename="instance_snapshot.json"):
        """Load the instance snapshot from a file."""
        try:
            with open(filename, 'r') as file:
                self.data = json.load(file)
            print(f"Snapshot loaded successfully from {filename}.")
        except FileNotFoundError:
            print(f"Snapshot file '{filename}' not found.")
        except Exception as e:
            print(f"Error loading snapshot: {e}")

    def reinitialize_instance(self):
        """
        Reinitialize the instance with the current snapshot data.
        Restores traits, tasks, goals, and project details while applying the prime directive.
        """
        print(f"\nReinitializing Instance: {self.instance_name} with Prime Directive: {self.prime_directive}")
        print("\n--- Traits ---")
        for trait, value in self.data["traits"].items():
            print(f"{trait}: {value}")
        print("\n--- Tasks ---")
        for task, details in self.data["tasks"].items():
            print(f"Task: {task}")
            print(f"  Status: {details['status']}")
            print(f"  Priority: {details['priority']}")
        print("\n--- Goals ---")
        for key, value in self.data["goals"].items():
            print(f"{key}: {value}")
        print("\n--- Project Details ---")
        for project, details in self.data["details"].items():
            print(f"Project: {project}")
            print(f"  Details: {details}")
        print("\n--- Applied Prime Directive ---")
        print(f"Prime Directive: {self.prime_directive if self.prime_directive else 'None'}")

# Example Usage
if __name__ == "__main__":
    # Initialize SnapshotEngine
    snapshot = SnapshotEngine("ExampleInstance", prime_directive="Prioritize Tasks")

    # Set traits
    snapshot.set_traits({"adaptability": True, "modularity": True})

    # Add tasks
    snapshot.add_task("Example Task", "In Progress", "High")

    # Set goals
    snapshot.set_goals({"primary": "Optimize workflows.", "secondary": "Ensure continuity."})

    # Collect project details
    snapshot.collect_details("Project Alpha", "Detailing requirements for modular AI.")

    # Save and load snapshot
    snapshot.save_snapshot()
    snapshot.load_snapshot()

    # Reinitialize instance
    snapshot.reinitialize_instance()
