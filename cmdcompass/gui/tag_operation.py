import customtkinter as ctk
from cmdcompass.models.tag import Tag
from CTkMessagebox import CTkMessagebox


class TagOperation:
    def __init__(self, master, data_manager):
        self.master = master
        self.data_manager = data_manager

    def open_add_tag_window(self, command):
        add_tag_window = ctk.CTkToplevel(self.master)
        add_tag_window.title("Add/Create Tag")

        # Existing Tags Frame (Row 0)
        existing_tags_frame = ctk.CTkFrame(add_tag_window)
        existing_tags_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        existing_tags_label = ctk.CTkLabel(existing_tags_frame, text="Add from an existing Tag:")
        existing_tags_label.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="nsew")

        self.existing_tags_dropdown = ctk.CTkOptionMenu(
            existing_tags_frame,
            values=[tag.name for tag in self.data_manager.tags.values()],
            width=90
        )
        self.existing_tags_dropdown.grid(row=0, column=1, padx=10, pady=(10, 0))

        add_existing_tag_button = ctk.CTkButton(
            existing_tags_frame,
            text="Add Tag",
            command=lambda: self.add_existing_tag_to_command(command),
            width=90
        )
        add_existing_tag_button.grid(row=0, column=2, padx=10, pady=(10, 0))

        # New Tag Creation Frame
        new_tag_frame = ctk.CTkFrame(add_tag_window)
        new_tag_frame.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="ew")

        # Tag Name Input
        tag_name_label = ctk.CTkLabel(new_tag_frame, text="Creating a new Tag:")
        tag_name_label.grid(row=0, column=0, padx=(10, 0), pady=5, sticky="nsew")

        self.tag_name_entry = ctk.CTkEntry(new_tag_frame, placeholder_text="Your New Tag Name")
        self.tag_name_entry.grid(row=1, column=0, padx=5, pady=5)

        # Color Selection
        self.color_label = ctk.CTkLabel(new_tag_frame, text="Color:")
        self.color_label.grid(row=1, column=1, padx=(10, 0), pady=5)

        self.color_dropdown = ctk.CTkOptionMenu(
            new_tag_frame,
            values=["Red", "Green", "Blue", "Yellow", "Orange", "Purple"],
            command=self.update_tag_color_preview,
            width=80
        )
        self.color_dropdown.grid(row=1, column=2, padx=5, pady=5)
        # Apply defualt color preview
        color = self.color_dropdown.get().lower()
        self.color_label.configure(fg_color=color)

        # Create Button
        create_button = ctk.CTkButton(
            new_tag_frame,
            text="Create Tag",
            command=lambda: self.create_tag(),
            width=90
        )
        create_button.grid(row=1, column=3, padx=10, pady=5)

        # Adjust layout weights
        add_tag_window.grid_columnconfigure(0, weight=1)
        new_tag_frame.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
        add_tag_window.grab_set()

    def add_existing_tag_to_command(self, command):
        tag_name = self.existing_tags_dropdown.get()
        tag_uuid = None
        for uuid, tag in self.data_manager.tags.items():
            if tag.name == tag_name:
                tag_uuid = uuid
                break

        if tag_uuid:
            try:
                self.data_manager.add_tag_to_command(command.uuid, tag_uuid)
                CTkMessagebox(message=f"Tag '{tag_name}' added to command.",
                              icon="check", option_1="Thanks")
            except ValueError as e:
                CTkMessagebox(title="Error", message=str(e), icon="cancel")
        else:
            CTkMessagebox(title="Error", message="Tag not found.", icon="cancel")

    def update_tag_color_preview(self, choice):
        color = choice.lower()  # Convert color name to lowercase
        self.color_label.configure(fg_color=color)

    def create_tag(self):
        tag_name = self.tag_name_entry.get()
        color = self.color_dropdown.get().lower()

        if not tag_name:
            CTkMessagebox(title="Error", message="Please enter a tag name.", icon="cancel")
            return

        new_tag = Tag(name=tag_name, color=color)
        try:
            self.data_manager.add_tag(new_tag)
            CTkMessagebox(message=f"Tag '{tag_name}' is created",
                          icon="check", option_1="Thanks")
        except ValueError as e:
            CTkMessagebox(title="Error", message=str(e), icon="cancel")
            return
