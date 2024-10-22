import customtkinter as ctk
from cmdcompass.models.tag import Tag
from CTkMessagebox import CTkMessagebox
from cmdcompass.utils.utils import getScreenSize


class TagOperation:
    def __init__(self, master, data_manager):
        self.master = master
        self.data_manager = data_manager

    def open_add_tag_window(self, command):
        screenSize = getScreenSize()
        add_tag_window = ctk.CTkToplevel(self.master)
        add_tag_window.title("Add/Remove Tag for This Command")
        
        add_tag_window_width = 450
        add_tag_window_height = 200
        screenSize = getScreenSize()
        
        x = (screenSize["SCREEN_WIDTH"]/2) - (add_tag_window_width/2) + screenSize["CENTER_OFFSET"]
        y = (screenSize["SCREEN_HEIGHT"]/2) - (add_tag_window_height/2)

        add_tag_window.geometry('%dx%d+%d+%d' % (add_tag_window_width, add_tag_window_height, x, y))

        # Existing Tags Frame (Row 0)
        existing_tags_frame = ctk.CTkFrame(add_tag_window)
        existing_tags_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        existing_tags_label = ctk.CTkLabel(existing_tags_frame, text="Add from an existing Tag:")
        existing_tags_label.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="nsew", columnspan=2)

        existing_tags = [tag.name for tag in self.data_manager.tags.values()]
        if not existing_tags:
            existing_tags = ["Please defined your Tag first (top left)"]
        self.existing_tags_dropdown = ctk.CTkOptionMenu(
            existing_tags_frame,
            values=existing_tags,
            width=90
        )
        self.existing_tags_dropdown.grid(row=1, column=0, padx=10, pady=(10, 0))

        add_existing_tag_button = ctk.CTkButton(
            existing_tags_frame,
            text="Add Tag",
            command=lambda: self.add_existing_tag_to_command(command),
            width=90
        )
        add_existing_tag_button.grid(row=1, column=1, padx=10, pady=(10, 0))

        # Remove Tag Frame (Row 1)
        remove_tag_frame = ctk.CTkFrame(add_tag_window)
        remove_tag_frame.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="ew")

        remove_tag_label = ctk.CTkLabel(remove_tag_frame, text="Remove an existing Tag:")
        remove_tag_label.grid(row=0, column=0, padx=10, pady=(0, 0), sticky="nsew", columnspan=2)
        tag_names = [self.data_manager.tags[tag_id].name for tag_id in command.tag_ids]
        if not tag_names:
            tag_names = ["The Command has no Tag"]
        self.remove_tag_dropdown = ctk.CTkOptionMenu(
            remove_tag_frame,
            values=tag_names,
            width=90
        )
        self.remove_tag_dropdown.grid(row=1, column=0, padx=10, pady=(0, 0))

        remove_tag_button = ctk.CTkButton(
            remove_tag_frame,
            text="Remove Tag",
            command=lambda: self.remove_tag_from_command(command),
            width=90
        )
        remove_tag_button.grid(row=1, column=1, padx=10, pady=(0, 0))

        # Adjust layout weights
        add_tag_window.grid_columnconfigure(0, weight=1)
        remove_tag_frame.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
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
                self.master.refresh_command_list()
                self.refresh_remove_tag_dropdown(command)
            except ValueError as e:
                CTkMessagebox(title="Error", message=str(e), icon="cancel")
        else:
            CTkMessagebox(title="Error", message="Tag not found.", icon="cancel")

    def refresh_remove_tag_dropdown(self, command):
        tag_names = [self.data_manager.tags[tag_id].name for tag_id in command.tag_ids]
        if not tag_names:
            tag_names = ["The Command has no Tag"]
        self.remove_tag_dropdown.configure(values=tag_names)
        self.remove_tag_dropdown.set(tag_names[0])

    def remove_tag_from_command(self, command):
        tag_name = self.remove_tag_dropdown.get()
        tag_uuid = None
        for uuid, tag in self.data_manager.tags.items():
            if tag.name == tag_name:
                tag_uuid = uuid
                break

        if tag_uuid:
            try:
                self.data_manager.remove_tag_from_command(command.uuid, tag_uuid)
                CTkMessagebox(message=f"Tag '{tag_name}' removed from command.",
                              icon="check", option_1="Thanks")
                self.master.refresh_command_list()
                self.refresh_remove_tag_dropdown(command)
            except ValueError as e:
                CTkMessagebox(title="Error", message=str(e), icon="cancel")
        else:
            CTkMessagebox(title="Error", message="Tag not found.", icon="cancel")