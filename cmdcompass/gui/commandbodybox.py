import customtkinter as ctk
from cmdcompass.utils.utils import load_ctk_image

class CommandBodyBox(ctk.CTkFrame):
    def __init__(self, master, main_window, **kwargs):
        super().__init__(master, **kwargs)
        self.main_window = main_window

        self.grid_rowconfigure(0, weight=1)  # Make the textbox row expandable
        self.grid_columnconfigure(0, weight=1)  # Make the textbox column expandable

        self.command_textbox = ctk.CTkTextbox(self, height=100)
        self.command_textbox.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Save button
        self.save_button = ctk.CTkButton(self, image=load_ctk_image("save.png"), text="", command=self.save_command, width=20)

        # Bind text modification event
        self.command_textbox.bind("<<Modified>>", self.on_text_modified)

    def on_text_modified(self, event):
        current_text = self.command_textbox.get("1.0", "end-1c")  # Get text without newline
        if self.main_window.selected_command and current_text != self.main_window.selected_command.command_str:
            self.save_button.grid(row=0, column=1, padx=(0, 10), pady=10, sticky="ns")
        else:
            self.save_button.grid_forget()
        self.command_textbox.edit_modified(False)  # Reset modified flag

    def set_command(self, command):
        self.command_textbox.delete("0.0", ctk.END)  # Clear previous text
        if command:
            self.command_textbox.insert(ctk.END, command.command_str)
        else:
            self.command_textbox.insert(ctk.END, "")  # Clear if no command
        self.save_button.grid_forget()

    def save_command(self):
        if self.main_window.selected_command:
            new_command_str = self.command_textbox.get("1.0", "end-1c")
            self.main_window.selected_command.command_str = new_command_str
            self.main_window.data_manager.save_data()
            self.save_button.grid_forget()
            self.main_window.refresh_command_list()  # Refresh the command list
