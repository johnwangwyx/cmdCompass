import unittest
import os
import tempfile
import json

from cmdcompass.models.collection import Collection
from cmdcompass.models.command import Command
from cmdcompass.models.tag import Tag
from cmdcompass.data.datamanager import DataManager


class TestDataManager(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for testing
        self.temp_dir = tempfile.TemporaryDirectory()
        self.data_file = os.path.join(self.temp_dir.name, "test_data.json")
        self.data_manager = DataManager(self.data_file)
        # Copy the testing file over
        with open("test/test_data.json", "r") as f_in, open(self.data_file, "w") as f_out:
            f_out.write(f_in.read())

    def tearDown(self):
        # Clean up the temporary file
        self.temp_dir.cleanup()

    def test_load_data_from_json(self):
        # Copy the mock JSON data to the temporary file
        with open("test/test_data.json", "r") as f_in, open(self.data_file, "w") as f_out:
            f_out.write(f_in.read())

        self.data_manager.load_data()
        collections = self.data_manager.get_collections()
        self.assertEqual(len(collections), 1)
        self.assertEqual(collections[0].name, "Test Collection 1")

        # Check if tags are loaded correctly
        self.assertEqual(len(self.data_manager.tags), 3)
        self.assertIn("tag1", self.data_manager.tags)

    def test_save_data_to_json(self):
        command = Command("echo 'saved'", "Saved command", [])
        collection = Collection("Saved Collection", [command])
        self.data_manager.add_collection(collection)

        with open(self.data_file, "r") as f:
            data = json.load(f)
        self.assertIn("Saved Collection", data)

    def test_get_collections(self):
        # Load data from the mock JSON
        self.data_manager.load_data()

        collections = self.data_manager.get_collections()
        self.assertEqual(len(collections), 1)
        self.assertIsInstance(collections[0], Collection)

    def test_get_collection(self):
        self.data_manager.load_data()

        collection = self.data_manager.get_collection("Test Collection 1")
        self.assertIsInstance(collection, Collection)
        self.assertEqual(collection.name, "Test Collection 1")

    def test_add_command(self):
        self.data_manager.load_data()

        new_command = Command("echo 'new command'", "New test command", [])
        prev_len = len(self.data_manager.get_collection("Test Collection 1").commands)
        self.data_manager.add_command("Test Collection 1", new_command)

        collection = self.data_manager.get_collection("Test Collection 1")
        self.assertEqual(len(collection.commands), prev_len+1)  # Should have added one command

    def test_delete_command(self):
        self.data_manager.load_data()

        prev_len = len(self.data_manager.get_collection("Test Collection 1").commands)

        self.data_manager.delete_command("Test Collection 1", "command1")
        collection = self.data_manager.get_collection("Test Collection 1")
        self.assertEqual(len(collection.commands), prev_len-1)  # Should have deleted the command

    def test_update_command(self):
        self.data_manager.load_data()

        updated_command = Command("echo 'updated'", "Updated command", [], uuid="command1")
        self.data_manager.update_command("Test Collection 1", "command1", updated_command)
        collection = self.data_manager.get_collection("Test Collection 1")
        self.assertEqual(collection.commands[0].command_str, "echo 'updated'")

    def test_add_tag(self):
        new_tag = Tag("New Tag", "purple")
        self.data_manager.add_tag(new_tag)
        self.assertIn(new_tag.uuid, self.data_manager.tags)
        self.assertEqual(self.data_manager.tags[new_tag.uuid].name, "New Tag")

    def test_add_tag_duplicate(self):
        # Load data from the mock JSON
        self.data_manager.load_data()

        existing_tag = Tag("Utility", "yellow")
        with self.assertRaises(ValueError):
            self.data_manager.add_tag(existing_tag)  # Should raise error for duplicate name

    def test_remove_tag(self):
        # Load data from the mock JSON
        self.data_manager.load_data()

        self.data_manager.remove_tag("tag2")  # Remove existing tag
        self.assertNotIn("tag2", self.data_manager.tags)

    def test_remove_tag_not_found(self):
        with self.assertRaises(ValueError):
            self.data_manager.remove_tag("nonexistent_tag")

    def test_add_tag_to_command(self):
        # Load data from the mock JSON
        self.data_manager.load_data()        
        
        self.data_manager.add_tag_to_command("command2", "tag3")
        collection = self.data_manager.get_collection("Test Collection 1")
        command = collection.commands[0]
        self.assertIn("tag3", command.tag_ids)

    def test_remove_tag_from_command(self):
        # Load data from the mock JSON
        self.data_manager.load_data()

        self.data_manager.remove_tag_from_command("command1", "tag2")
        collection = self.data_manager.get_collection("Test Collection 1")
        command = collection.commands[0]
        self.assertNotIn("tag2", command.tag_ids)

if __name__ == "__main__":
    unittest.main()