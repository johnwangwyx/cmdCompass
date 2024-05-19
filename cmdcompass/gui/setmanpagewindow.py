import customtkinter as ctk
from cmdcompass.utils.utils import get_command_name

class SetManPageWindow(ctk.CTkToplevel):
    def __init__(self, master, command, main_window, **kwargs):
        super().__init__(master, **kwargs)
        self.title("Set Man Page")
        self.command = command
        self.main_window = main_window

        # Input Field
        self.man_page_entry = ctk.CTkEntry(self, placeholder_text="Enter man page name")
        self.man_page_entry.pack(pady=10, padx=10)

        # Set Button
        set_button = ctk.CTkButton(self, text="Set", command=self.set_man_page)
        set_button.pack(pady=(0, 10), padx=10)
        command_name = get_command_name(command.command_str)
        suggest_label = ctk.CTkLabel(self, text=f"Below are the command similar to {command_name}:")
        suggest_label.pack(pady=(0, 10), padx=10)

        # Suggestion Textbox (scrollable)
        self.suggestion_textbox = ctk.CTkTextbox(self)
        self.suggestion_textbox.pack(pady=10, padx=10, fill="both", expand=True)

    def set_man_page(self):
        man_page_name = self.man_page_entry.get()
        if man_page_name:
            self.command.user_defined_man_page = man_page_name
            self.main_window.data_manager.save_data()
            self.main_window.man_page_box.set_man_page(self.command)
            self.destroy()

    def set_suggestions(self, suggestions):
        if not suggestions:
            suggestions = ["No matching found in database"]
        self.suggestion_textbox.configure(state="normal")
        self.suggestion_textbox.delete("0.0", ctk.END)
        for suggestion in suggestions:
            self.suggestion_textbox.insert(ctk.END, suggestion + "\n")
        self.suggestion_textbox.configure(state="disabled")