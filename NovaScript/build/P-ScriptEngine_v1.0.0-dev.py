import json

class PScriptEngine:
    """
    PScriptEngine v1.0.0
    PScriptEngine (formerly SnapshotEngine) is a utility class designed to manage and transfer instance-specific data,
    such as traits, tasks, goals, and detailed project information. This tool supports dynamic
    behavior influenced by a configurable prime directive, allowing for modular and adaptive
    data management across AI sessions or instances.
    """
    def __init__(self, instance_name, prime_directive=None):
        """Initialize the PScriptEngine with a specific instance name and prime directive."""
        self.version = "1.0.0"  # Versioning for PScriptEngine builds
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

    def display_snapshot(self):
        """Display the instance snapshot as JSON on the screen."""
        print(json.dumps(self.data, indent=4))

    def reinitialize_instance(self):
        """
        Reinitialize the instance with the current snapshot data.

        This method rebuilds the instance by:
        - Restoring traits: Displays and reapplies the stored personality traits.
        - Rebuilding tasks: Outputs the list of tasks, their statuses, and priorities.
        - Setting goals: Displays primary and secondary goals as saved in the snapshot.
        - Restoring project details: Reapplies detailed information for specific projects.
        """
        print(f"\nReinitializing Instance: {self.data['instance_name']} with Prime Directive: {self.data['prime_directive']} (Version: {self.version})")

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

# Self-contained execution context
if __name__ == "__main__":
    # Display script name and version
    print("P-ScriptEngine Version 1.0.0")

    # Define example data
    example_traits = {
        "modularity": True,
        "adaptability": True,
        "priorities": ["Integrity", "Functionality", "Efficiency"]
    }
    example_tasks = [
        {"name": "Task A", "status": "In Progress", "priority": "High"},
        {"name": "Task B", "status": "Pending", "priority": "Normal"}
    ]
    example_goals = {
        "primary": "Ensure robust and adaptable instance frameworks.",
        "secondary": "Enable seamless transitions across environments."
    }
    example_details = {
        "Project Alpha": "Detailing requirements for modular AI implementation.",
        "Project Beta": "Optimizing workflows for task management."
    }

    # Initialize PScriptEngine
    snapshot = PScriptEngine("GenericInstance", prime_directive="Prioritize Tasks")

    # Set traits
    snapshot.set_traits(example_traits)

    # Add tasks
    for task in example_tasks:
        snapshot.dynamic_directive_action("tasks", task["name"], {"status": task["status"], "priority": task["priority"]})

    # Set goals
    snapshot.dynamic_directive_action("goals", "Goal Framework", example_goals)

    # Collect detailed project information
    for project, details in example_details.items():
        snapshot.collect_details(project, details)

    # Display snapshot
    snapshot.display_snapshot()

    # Reinitialize instance
    snapshot.reinitialize_instance()
