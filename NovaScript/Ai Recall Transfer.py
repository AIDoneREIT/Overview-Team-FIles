import json

class SnapshotEngine:
    """
    SnapshotEngine is a utility class designed to manage and transfer instance-specific data,
    such as traits, tasks, goals, and detailed project information. This tool supports dynamic
    behavior influenced by a configurable prime directive, allowing for modular and adaptive
    data management across AI sessions or instances.
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
        self.data["tasks"][task_name] = {
            "status": status,
            "priority": priority
        }

    def set_goals(self, goals):
        """Define the overarching goals for the instance."""
        self.data["goals"] = goals

    def collect_details(self, project_name, details):
        """Collect and store detailed information for a specific project."""
        self.data["details"][project_name] = details

    def dynamic_directive_action(self, data_type, key, value):
        """
        Leverage the prime directive to dynamically modify data.

        This method applies the instance's prime directive to adjust tasks, goals, or other data types
        dynamically based on their attributes. For example, tasks marked as high priority are escalated
        to urgent status, or goals are refined to align with optimization strategies.

        Args:
            data_type (str): The type of data being modified (e.g., "tasks", "goals").
            key (str): The unique identifier for the data item (e.g., task name or goal key).
            value (dict): The data to be modified, containing relevant attributes like "status" or "priority".

        Returns:
            None

        Examples:
            If the prime directive is "Prioritize Tasks", high-priority tasks are flagged as urgent:
            ```python
            task = {"status": "Pending", "priority": "High"}
            dynamic_directive_action("tasks", "Task A", task)
            ```
        """
        if self.prime_directive == "Prioritize Tasks":
            if data_type == "tasks":
                # Automatically elevate priority for critical tasks
                if value.get("priority") == "High":
                    value["status"] = "Urgent"
        elif self.prime_directive == "Optimize Goals":
            if data_type == "goals":
                # Automatically refine goals for clarity
                value["primary"] = f"Optimized: {value.get('primary', '')}"

        # Apply changes to the relevant data structure
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

        This method rebuilds the instance by:
        - Restoring traits: Displays and reapplies the stored personality traits.
        - Rebuilding tasks: Outputs the list of tasks, their statuses, and priorities.
        - Setting goals: Displays primary and secondary goals as saved in the snapshot.
        - Restoring project details: Reapplies detailed information for specific projects.

        The reinitialization process ensures continuity by leveraging the saved snapshot
        data and applying any modifications guided by the prime directive.
        """
        print(f"\nReinitializing Instance: {self.data['instance_name']} with Prime Directive: {self.data['prime_directive']}")

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
    # Initialize SnapshotEngine with instance name and prime directive
    snapshot = SnapshotEngine("GenericInstance", prime_directive="Prioritize Tasks")

    # Define traits
    traits = {
        "modularity": True,
        "adaptability": True,
        "priorities": ["Integrity", "Functionality", "Efficiency"]
    }
    snapshot.set_traits(traits)

    # Add tasks with dynamic directive influence
    task_a = {"status": "In Progress", "priority": "High"}
    snapshot.dynamic_directive_action("tasks", "Task A", task_a)

    task_b = {"status": "Pending", "priority": "Normal"}
    snapshot.dynamic_directive_action("tasks", "Task B", task_b)

    # Set goals
    goals = {
        "primary": "Ensure robust and adaptable instance frameworks.",
        "secondary": "Enable seamless transitions across environments."
    }
    snapshot.dynamic_directive_action("goals", "Goal Framework", goals)

    # Collect detailed project information
    snapshot.collect_details("Project Alpha", "Detailing requirements for modular AI implementation.")
    snapshot.collect_details("Project Beta", "Optimizing workflows for task management.")

    # Save snapshot
    snapshot.save_snapshot()

    # Load snapshot and reinitialize
    snapshot.load_snapshot()
    snapshot.reinitialize_instance()
