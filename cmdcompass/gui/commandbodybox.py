import customtkinter as ctk
from cmdcompass.utils.utils import load_ctk_image

class CommandBodyBox(ctk.CTkFrame):
    def __init__(self, master, main_window, **kwargs):
        super().__init__(master, **kwargs)
        self.main_window = main_window

        self.grid_rowconfigure(0, weight=1)  # Make the textbox row expandable
        self.grid_columnconfigure(0, weight=1)  # Make the textbox column expandable

        self.command_textbox = ctk.CTkTextbox(self, height=100, wrap='word')
        self.command_textbox.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Copy button
        self.copy_button = ctk.CTkButton(self, image=load_ctk_image("copy.png"), text="", command=self.copy_command, width=20)
        self.copy_button.grid(row=0, column=1, padx=(0, 5), pady=10, sticky = "ns")

        # Save button
        self.save_button = ctk.CTkButton(self, image=load_ctk_image("save.png"), text="", command=self.save_command, width=20, fg_color="orange")
        self.save_button.grid(row=0, column=2, padx=(0, 5), pady=10, sticky="ns")
        self.default_color = "orange"
        self.save_button.configure(state="disabled", fg_color="gray")

        # Bind text modification event
        self.command_textbox.bind("<<Modified>>", self.on_text_modified)

    def on_text_modified(self, event):
        current_text = self.command_textbox.get("1.0", "end-1c")  # Get text without newline
        if self.main_window.selected_command and current_text != self.main_window.selected_command.command_str:
            self.save_button.configure(state="normal", fg_color=self.default_color)
        else:
            self.save_button.configure(state="disabled", fg_color="gray")
        self.command_textbox.edit_modified(False)  # Reset modified flag

    def set_command(self, command):
        self.command_textbox.delete("0.0", ctk.END)  # Clear previous text
        if command:
            self.command_textbox.insert(ctk.END, command.command_str)
        else:
            self.command_textbox.insert(ctk.END, "")  # Clear if no command
        self.save_button.configure(state="disabled", fg_color="gray")

    def save_command(self, save_only=False):
        if hasattr(self.main_window, "selected_command") and self.main_window.selected_command:
            new_command_str = self.command_textbox.get("1.0", "end-1c")
            new_command_str = new_command_str.replace('\u2212', '-')  # Minus sign should be dash
            self.main_window.selected_command.command_str = new_command_str
            if '\u2212' in self.command_textbox.get("1.0", "end-1c"):
                self.set_command(self.main_window.selected_command)
            self.main_window.data_manager.save_data()
            self.main_window.refresh_command_list()  # Refresh the command list
            if not save_only:
                self.save_button.configure(state="disabled", fg_color="gray")
                self.main_window.utility_box.set_command(self.main_window.selected_command)
                if self.main_window.active_tab == "man_page":
                    self.main_window.man_page_box.set_man_page(self.main_window.selected_command)

    def copy_command(self):
        command_str = self.command_textbox.get("1.0", "end-1c")
        # Copy the generated command to clipboard
        self.master.master.clipboard_clear()
        self.master.master.clipboard_append(command_str)