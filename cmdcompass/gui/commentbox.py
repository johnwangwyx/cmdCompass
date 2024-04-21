import customtkinter as ctk

class CommentBox(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.comment_textbox = ctk.CTkTextbox(self)
        self.comment_textbox.pack(padx=10, pady=10, fill="both", expand=True)

    def set_comment(self, comment):
        self.comment_textbox.delete("0.0", ctk.END)
        if comment:
            self.comment_textbox.insert(ctk.END, comment)
        else:
            self.comment_textbox.insert(ctk.END, "")  # Clear if no comment
