import unittest
from src.SnapshotEngine import SnapshotEngine

class TestSnapshotEngine(unittest.TestCase):
    def test_initialization(self):
        instance = SnapshotEngine("TestInstance")
        self.assertEqual(instance.instance_name, "TestInstance")

    def test_add_task(self):
        instance = SnapshotEngine("TestInstance")
        instance.add_task("Task 1", "In Progress", "High")
        self.assertIn("Task 1", instance.data["tasks"])

if __name__ == "__main__":
    unittest.main()
