import customtkinter as ctk

class TagBox(ctk.CTkFrame):
    def __init__(self, master, tags, command, main_window,**kwargs):
        super().__init__(master, **kwargs)
        # Add Tag button
        self.add_tag_button = ctk.CTkButton(
            self,
            text="+",
            font=("TkDefaultFont ", 8),
            width=15,
            height=3,
            command=lambda: main_window.open_add_tag_window(command)
        )
        self.add_tag_button.grid(row=0, column=0, padx=(0, 0), pady=2)
        self.add_tag_button.configure(corner_radius=3)
        for i, tag in enumerate(tags):
            tag_label = ctk.CTkLabel(self, text=f"{tag.name}", fg_color=tag.color, font=("TkDefaultFont ", 9), height=15)
            tag_label.configure(corner_radius=8)
            tag_label.grid(row=0, column=i+1, padx=(2, 0), pady=2)

class CommandBox(ctk.CTkFrame):
    def __init__(self, master, command, tags, command_index, main_window, **kwargs):
        super().__init__(master, **kwargs)
        self.command = command
        self.command_index = command_index
        self.main_window = main_window

        # Command label (first row)
        command_summery = command.command_str
        if len(command_summery) > 25:
            command_summery = command_summery[:25] + "..."
        self.command_label = ctk.CTkLabel(self, text=command_summery,  font=("TkDefaultFont", 12))
        self.command_label.grid(row=0, column=0, padx=10, pady=0, sticky="w")

        # Tag box (second row, first column)
        tag_box = TagBox(self, tags, command, main_window)
        tag_box.grid(row=1, column=0, padx=10, pady=(0, 5))

        # Select button
        self.select_button = ctk.CTkButton(
            self,
            text=">",
            width=20,
            height=40,
            command=lambda: self.main_window.on_command_select(self.command_index)
        )
        self.select_button.grid(row=0, column=1, rowspan=2, padx=(2, 3), pady=2, sticky="ns")

        # Adjust column weights
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
