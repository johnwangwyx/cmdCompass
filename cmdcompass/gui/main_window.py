import customtkinter as ctk
from cmdcompass.data.datamanager import DataManager
from cmdcompass.gui.commandbox import CommandBox
from cmdcompass.gui.commentbox import CommentBox
from cmdcompass.gui.commandbodybox import CommandBodyBox
from cmdcompass.gui.tagoperationbox import TagOperationBox
from cmdcompass.gui.utilitybox import UtilityBox

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("cmdCompass")
        self.geometry("900x650")

        # Load data
        self.data_manager = DataManager()
        self.data_manager.load_data()
        self.collections = self.data_manager.get_collections()

        # Create main frames
        self.left_frame = ctk.CTkFrame(self)
        self.right_frame = ctk.CTkFrame(self)

        # Layout frames
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.grid_rowconfigure(0, weight=1)
        # Adjust layout weights
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=30)

        # Collection label
        collection_label = ctk.CTkLabel(self.left_frame, text="Collections")
        collection_label.grid(row=0, column=0, padx=10, pady=(10, 0))

        # Collection dropdown
        self.collection_dropdown = ctk.CTkOptionMenu(
            self.left_frame, 
            values=[collection.name for collection in self.collections],
            command=self.on_collection_select
        )
        self.collection_dropdown.grid(row=1, column=0, padx=10, pady=10)
        
        # Create scrollable frame for the command list
        self.command_list_frame = ctk.CTkScrollableFrame(self.left_frame, height=450)
        self.command_list_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # Command list (using CTkTextbox inside the scrollable frame)
        self.command_list_box = ctk.CTkTextbox(self.command_list_frame)
        self.command_list_box.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="nsew")

        # Configure scrolling behavior
        self.command_list_frame.configure(corner_radius=5)
        self.command_list_box.configure(fg_color="transparent")  # Make textbox background transparent

        self.theme_toggle_button = ctk.CTkSwitch(
            self.left_frame,
            text="Light Mode",
            command=self.toggle_theme
        )
        self.theme_toggle_button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

        # Right Pane Boxes (using imported classes)
        self.command_body_box = CommandBodyBox(self.right_frame)
        self.command_body_box.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.tag_operation_box = TagOperationBox(self.right_frame, width=70)
        self.tag_operation_box.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.utility_box = UtilityBox(self.right_frame)
        self.utility_box.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.comment_box = CommentBox(self.right_frame)
        self.comment_box.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Adjust layout weights for right pane
        self.right_frame.grid_rowconfigure((0,1,2), weight=1)
        self.right_frame.grid_columnconfigure(0, weight=4)

    def on_collection_select(self, choice):
        selected_collection = self.data_manager.get_collection(choice)
        if selected_collection:
            self.update_command_list(selected_collection.commands)

    def update_command_list(self, commands):
        for child in self.command_list_frame.winfo_children():
            child.destroy()  # Clear previous command boxes

        for command in commands:
            tags = [self.data_manager.tags[tag_id] for tag_id in command.tag_ids]
            command_box = CommandBox(self.command_list_frame, command, tags)
            command_box.pack(pady=5, padx=10, fill="x")

    def toggle_theme(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("light")
            self.theme_toggle_button.configure(text="Light Mode")
        else:
            ctk.set_appearance_mode("Dark")
            self.theme_toggle_button.configure(text="Dark Mode")

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
