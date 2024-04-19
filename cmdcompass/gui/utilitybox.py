import customtkinter as ctk

class UtilityBox(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        placeholder_label = ctk.CTkLabel(self, text="Utilities")
        placeholder_label.pack(padx=10, pady=10)