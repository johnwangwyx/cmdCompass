import customtkinter as ctk
from cmdcompass.utils.utils import load_ctk_image

class CommentBox(ctk.CTkFrame):
    def __init__(self, master, main_window, **kwargs):
        super().__init__(master, **kwargs)
        self.main_window = main_window
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.comment_textbox = ctk.CTkTextbox(self, height=350)
        self.comment_textbox.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.save_button = ctk.CTkButton(self, image=load_ctk_image("save.png"), text="", command=self.save_comment, width=20)

        # Bind text modification event
        self.comment_textbox.bind("<<Modified>>", self.on_text_modified)

    def on_text_modified(self, event):
        current_text = self.comment_textbox.get("1.0", "end-1c")
        if self.main_window.selected_command and current_text != self.main_window.selected_command.comment:
            self.save_button.grid(row=0, column=1, padx=(10, 0), pady=0, sticky="ns")
        else:
            self.save_button.grid_forget()
        self.comment_textbox.edit_modified(False)

    def set_comment(self, comment):
        self.comment_textbox.delete("0.0", ctk.END)
        if comment:
            self.comment_textbox.insert(ctk.END, comment)
        else:
            self.comment_textbox.insert(ctk.END, "")  # Clear if no comment
        self.save_button.grid_forget()  # Hide the button initially

    def save_comment(self):
        if self.main_window.selected_command:
            new_comment = self.comment_textbox.get("1.0", "end-1c")
            self.main_window.selected_command.comment = new_comment
            self.main_window.data_manager.save_data()
            self.save_button.grid_forget()
            self.main_window.refresh_command_list()
