import customtkinter as ctk

class TagBox(ctk.CTkFrame):
    def __init__(self, master, tags, **kwargs):
        super().__init__(master, **kwargs)
        for i, tag in enumerate(tags):
            tag_label = ctk.CTkLabel(self, text=f"{tag.name}", fg_color=tag.color, font=("TkDefaultFont ", 8), height=15)
            tag_label.configure(corner_radius=8)
            tag_label.grid(row=0, column=i, padx=(2, 0), pady=2)

class CommandBox(ctk.CTkFrame):
    def __init__(self, master, command, tags, **kwargs):
        super().__init__(master, **kwargs)
        self.command = command

        # Command label (first row)
        self.command_label = ctk.CTkLabel(self, text=command.command_str.split(" ")[0] + "...",  font=("TkDefaultFont", 12))
        self.command_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Tag box (second row, first column)
        tag_box = TagBox(self, tags)
        tag_box.grid(row=1, column=0, padx=10, pady=(0, 5))
