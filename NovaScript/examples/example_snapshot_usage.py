from src.SnapshotEngine import SnapshotEngine

# Example usage of SnapshotEngine
snapshot = SnapshotEngine("DemoInstance", prime_directive="Optimize Goals")
snapshot.set_traits({"scalability": True, "efficiency": True})
snapshot.add_task("Demo Task", "Pending", "High")
snapshot.save_snapshot()
snapshot.load_snapshot()
snapshot.reinitialize_instance()
