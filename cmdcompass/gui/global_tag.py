import customtkinter as ctk
from cmdcompass.models.tag import Tag
from CTkMessagebox import CTkMessagebox

TAG_COLORS = ["Orange", "Cyan", "Azure", "Yellow", "Pink", "Green", "Red", "Purple", "Gray"]


class GlobalTagWindow(ctk.CTkToplevel):
    def __init__(self, master, data_manager):
        super().__init__(master)
        self.title("Create New Tag")
        self.data_manager = data_manager

        # Main frame to hold everything
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Create Tag Frame
        create_tag_frame = ctk.CTkFrame(main_frame)
        create_tag_frame.pack(pady=0, fill="x")

        # Tag Name Input
        tag_name_label = ctk.CTkLabel(create_tag_frame, text="Tag Name:")
        tag_name_label.grid(row=0, column=0, padx=(10, 0), pady=5)

        self.tag_name_entry = ctk.CTkEntry(create_tag_frame)
        self.tag_name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Color Selection
        self.color_label = ctk.CTkLabel(create_tag_frame, text="Color:")
        self.color_label.grid(row=1, column=0, padx=(10, 0), pady=5)

        self.color_dropdown = ctk.CTkOptionMenu(
            create_tag_frame,
            values=TAG_COLORS,
            command=self.update_tag_color_preview
        )
        self.color_dropdown.grid(row=1, column=1, padx=5, pady=5)

        # Color Preview
        self.color_label.configure(fg_color=TAG_COLORS[0].lower())
        self.color_label.configure(corner_radius=12)

        # Create Button
        create_button = ctk.CTkButton(
            create_tag_frame,
            text="Create Tag",
            command=self.create_tag
        )
        create_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        # Remove Tags Frame
        remove_tags_frame = ctk.CTkFrame(main_frame)
        remove_tags_frame.pack(pady=30, fill="both", expand=True)

        remove_tags_label = ctk.CTkLabel(remove_tags_frame, text="Existing Tags:")
        remove_tags_label.pack(pady=(0, 10))

        # Scrollable frame for tag list
        self.tag_list_frame = ctk.CTkScrollableFrame(remove_tags_frame)
        self.tag_list_frame.pack(fill="both", expand=True)
        self.update_tag_list()

        # Adjust layout weights
        main_frame.grid_columnconfigure(0, weight=1)

    def update_tag_color_preview(self, choice):
        color = choice.lower()
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
            CTkMessagebox(message=f"Tag '{tag_name}' created successfully.",
                          icon="check", option_1="Thanks")
        except ValueError as e:
            CTkMessagebox(title="Error", message=str(e), icon="cancel")
        self.update_tag_list()  # Refresh the tag list

    def update_tag_list(self):
        for child in self.tag_list_frame.winfo_children():
            child.destroy()

        for tag_uuid, tag in self.data_manager.tags.items():
            tag_frame = ctk.CTkFrame(self.tag_list_frame)
            tag_frame.pack(fill="x", pady=5, padx=10)

            tag_label = ctk.CTkLabel(tag_frame, text=tag.name, fg_color=tag.color)
            tag_label.configure(corner_radius=12)
            tag_label.pack(side=ctk.LEFT)

            remove_button = ctk.CTkButton(
                tag_frame,
                text="x",
                width=30,
                fg_color="red",
                hover_color="#c77c78",
                command=lambda uuid=tag_uuid: self.remove_tag(uuid)
            )
            remove_button.pack(side=ctk.RIGHT)  # Right align the button

    def remove_tag(self, tag_uuid):
        tag_name = self.data_manager.tags[tag_uuid].name

        # Check if the tag is used by any commands
        for collection in self.data_manager.data.values():
            for command in collection.commands:
                if tag_uuid in command.tag_ids:
                    CTkMessagebox(title="Error",
                                  message=f"Cannot remove tag '{tag_name}'. It is currently associated with commands.",
                                  icon="cancel")
                    return  # Don't remove the tag

        # If the tag is not used, proceed with removal
        try:
            self.data_manager.remove_tag(tag_uuid)
            self.update_tag_list()  # Refresh the tag list
        except ValueError as e:
            CTkMessagebox(title="Error", message=str(e), icon="cancel")
