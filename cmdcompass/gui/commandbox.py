import customtkinter as ctk
import tkinter.font as tkFont

COMMAND_LABLE_WIDTH = 200

class TagBox(ctk.CTkFrame):
    def __init__(self, master, tags, command, main_window,**kwargs):
        super().__init__(master, **kwargs)
        # Add Tag button
        self.add_tag_button = ctk.CTkButton(
            self,
            text="tag",
            font=("TkDefaultFont ", 8),
            width=15,
            height=3,
            command=lambda: main_window.open_add_tag_window(command)
        )
        self.add_tag_button.grid(row=0, column=0, padx=(0, 0), pady=2)
        self.add_tag_button.configure(corner_radius=3)
        for i, tag in enumerate(tags):
            tag_label = ctk.CTkLabel(self, text=f"{tag.name}", fg_color=tag.color, text_color="black", font=("TkDefaultFont ", 9), height=15)
            tag_label.configure(corner_radius=8)
            tag_label.grid(row=0, column=i+1, padx=(2, 0), pady=2)

class CommandBox(ctk.CTkFrame):
    def __init__(self, master, command, tags, command_index, main_window, **kwargs):
        super().__init__(master, **kwargs)
        self.command = command
        self.command_index = command_index
        self.main_window = main_window

        # Frame for delete button
        self.delete_button_frame = ctk.CTkFrame(self)
        self.delete_button_frame.place(relx=0, rely=0, anchor="nw")  # Position relative to CommandBox

        # Delete button
        self.delete_button = ctk.CTkButton(
            self.delete_button_frame,
            text="X",
            width=7,
            height=7,
            fg_color="red",
            hover_color="#c77c78",
            font=("TkDefaultFont ", 9),
            command=lambda: self.main_window.delete_command(self.command_index)
        )
        self.delete_button.pack()
        self.delete_button.configure(corner_radius=5)
        cmd_summary = command.command_str[:33]
        font =tkFont.Font(family="TkDefaultFont", size=12)
        text_width = font.measure(cmd_summary)

        # Reduce text until it fits the given pixel width
        while text_width > COMMAND_LABLE_WIDTH:
            cmd_summary = cmd_summary[:-1]
            text_width = font.measure(cmd_summary + '...')
        if cmd_summary != command.command_str:
            cmd_summary += "..."
        self.command_label = ctk.CTkLabel(self, text=cmd_summary,  font=("TkDefaultFont", 12))
        self.command_label.grid(row=0, column=0, padx=(20,0), pady=0, sticky="w")

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
        self.select_button.grid(row=0, column=1, rowspan=2, padx=(0, 3), pady=2, sticky="ns")

        # Adjust column weights
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
