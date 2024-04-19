import customtkinter as ctk

class TagOperationBox(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        placeholder_label = ctk.CTkLabel(self, text="Tag Operations")
        placeholder_label.pack(padx=10, pady=10)