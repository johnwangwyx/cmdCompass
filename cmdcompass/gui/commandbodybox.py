import customtkinter as ctk

class CommandBodyBox(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.command_textbox = ctk.CTkTextbox(self)
        self.command_textbox.pack(padx=10, pady=10, fill="both", expand=True)