import json
from typing import List, Dict

from cmdcompass.models.collection import Collection
from cmdcompass.models.command import Command
from cmdcompass.models.tag import Tag

class DataManager:
    def __init__(self, data_file="./data/data.json"):
        self.data_file = data_file
        self.data: Dict[str, Collection] = {}  # {collection_name: Collection object}
        self.load_data()
        self.tags: Dict[str, Tag] = {}  # Store tags by UUID

    def load_data(self):
        """Loads data from the JSON file and parses tags."""
        try:
            with open(self.data_file, "r") as f:
                raw_data = json.load(f)

                # Load tags first
                self.tags = {tag_data["uuid"]: Tag(**tag_data) for tag_data in raw_data.get("tags", [])}

                for collection_name, collection_data in raw_data.items():
                    if collection_name == "tags":
                        continue  # Skip the "tags" section

                    commands = []
                    for cmd_data in collection_data["commands"]:
                        commands.append(Command(**cmd_data))

                    self.data[collection_name] = Collection(
                        name=collection_name,
                        commands=commands
                    )
        except FileNotFoundError:
            # File doesn't exist yet, create an empty data structure
            self.data = {}

    def save_data(self):
        """Saves data to the JSON file."""
        with open(self.data_file, "w") as f:
            json_data = {
                "tags": [tag.__dict__ for tag in self.tags.values()],  # Save tags separately
                **{
                    collection.name: {
                        "commands": [cmd.__dict__ for cmd in collection.commands]
                    } 
                    for collection in self.data.values()
                }
            }
            json.dump(json_data, f, indent=4)

    # ------------------Collection-----------------
    def get_collections(self) -> List[Collection]:
        """Returns a list of all collections."""
        return list(self.data.values())

    def get_collection(self, collection_name: str) -> Collection:
        """Returns a specific collection by name."""
        return self.data.get(collection_name)

    def add_collection(self, collection: Collection):
        """Adds a new collection, ensuring no duplicates by name."""
        if collection.name in self.data:
            raise ValueError(f"Collection with name '{collection.name}' already exists.")
        else:
            self.data[collection.name] = collection
            self.save_data()

    def delete_collection(self, collection_name: str):
        """Deletes a collection by name."""
        if collection_name in self.data:
            del self.data[collection_name]
            self.save_data()

    # ------------------Command-----------------
    def add_command(self, collection_name: str, command: Command):
        """Adds a new command to a collection."""
        collection = self.get_collection(collection_name)
        if collection:
            collection.commands.append(command)
            self.save_data()
        else:
            raise ValueError(f"Collection '{collection_name}' not found.")

    def delete_command(self, collection_name: str, command_uuid: str):
        """Deletes a command from a collection by UUID."""
        collection = self.get_collection(collection_name)
        if collection:
            for i, cmd in enumerate(collection.commands):
                if cmd.uuid == command_uuid:
                    del collection.commands[i]
                    self.save_data()
                    return
            raise ValueError(f"Command with UUID '{command_uuid}' not found in collection.")
        else:
            raise ValueError(f"Collection '{collection_name}' not found.")

    def update_command(self, collection_name: str, command_uuid: str, updated_command: Command):
        """Updates a command in a collection by UUID."""
        collection = self.get_collection(collection_name)
        if collection:
            for i, cmd in enumerate(collection.commands):
                if cmd.uuid == command_uuid:
                    collection.commands[i] = updated_command
                    self.save_data()
                    return
            raise ValueError(f"Command with UUID '{command_uuid}' not found in collection.")
        else:
            raise ValueError(f"Collection '{collection_name}' not found.")

    # ------------------Tag-----------------
    def add_tag(self, tag: Tag):
        """Adds a new tag, ensuring no duplicates by name."""
        if tag.name in [t.name for t in self.tags.values()]:
            raise ValueError(f"Tag with name '{tag.name}' already exists.")
        self.tags[tag.uuid] = tag
        self.save_data()

    def remove_tag(self, tag_uuid: str):
        """Removes a tag by UUID."""
        if tag_uuid in self.tags:
            del self.tags[tag_uuid]
            self.save_data()
        else:
            raise ValueError(f"Tag with UUID '{tag_uuid}' not found.")

    def add_tag_to_command(self, command_uuid: str, tag_uuid: str):
        """Adds a tag to a command."""
        for collection in self.data.values():
            for command in collection.commands:
                if command.uuid == command_uuid:
                    if tag_uuid not in command.tag_ids:
                        command.tag_ids.append(tag_uuid)
                        self.save_data()
                    return  # Exit after adding the tag
        raise ValueError(f"Command with UUID '{command_uuid}' not found.")

    def remove_tag_from_command(self, command_uuid: str, tag_uuid: str):
        """Removes a tag from a command."""
        for collection in self.data.values():
            for command in collection.commands:
                if command.uuid == command_uuid:
                    if tag_uuid in command.tag_ids:
                        command.tag_ids.remove(tag_uuid)
                        self.save_data()
                    return
        raise ValueError(f"Command with UUID '{command_uuid}' or tag with UUID '{tag_uuid}' not found.")
