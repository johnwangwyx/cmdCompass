import customtkinter as ctk

class CommandBodyBox(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.command_textbox = ctk.CTkTextbox(self, height=140)
        self.command_textbox.pack(padx=10, pady=10, fill="both", expand=True)

    def set_command(self, command):
        self.command_textbox.delete("0.0", ctk.END)  # Clear previous text
        if command:
            self.command_textbox.insert(ctk.END, command.command_str)
        else:
            self.command_textbox.insert(ctk.END, "")  # Clear if no command
