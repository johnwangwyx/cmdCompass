import unittest

from cmdcompass.models.collection import Collection
from cmdcompass.models.command import Command

class TestCollection(unittest.TestCase):
    def test_collection_creation(self):
        command = Command("echo 'test'", "Test command", [])
        collection = Collection("Test Collection", "Description", [command])
        self.assertEqual(collection.name, "Test Collection")
        self.assertEqual(len(collection.commands), 1)