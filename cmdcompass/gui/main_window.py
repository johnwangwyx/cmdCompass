import customtkinter as ctk
from cmdcompass.data.datamanager import DataManager
from cmdcompass.gui.commandbox import CommandBox

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("cmdCompass")
        self.geometry("800x600")

        # Load data
        self.data_manager = DataManager()
        self.data_manager.load_data()
        self.collections = self.data_manager.get_collections()

        # Create main frames
        self.left_frame = ctk.CTkFrame(self)
        self.right_frame = ctk.CTkFrame(self)

        # Layout frames
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=10)
        self.right_frame.grid(row=0, column=1, sticky="nsew")
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
        
    def on_collection_select(self, choice):
        selected_collection = self.data_manager.get_collection(choice)
        if selected_collection:
            self.update_command_list(selected_collection.commands)

    def update_command_list(self, commands):
        for child in self.command_list_frame.winfo_children():
            child.destroy()  # Clear previous command boxes

        for command in commands:
            command_box = CommandBox(self.command_list_frame, command)
            command_box.pack(pady=5, padx=10, fill="x")

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()