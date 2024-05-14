import customtkinter as ctk


class ProgressWindow(ctk.CTkToplevel):
    def __init__(self, master, title, **kwargs):
        super().__init__(master, **kwargs)
        self.title(title)
        self.geometry("700x200")

        self.progress_textbox = ctk.CTkTextbox(self)
        self.progress_textbox.pack(pady=20, padx=20, fill="both", expand=True)

        self.progressbar = ctk.CTkProgressBar(self, width=400)
        self.progressbar.pack(pady=10, padx=20)
        self.progressbar.set(0)  # Set initial progress to 0

    def update_progress(self, message="", value=-1):
        if value != -1:
            self.progressbar.set(value)
        if message:
            self.progress_textbox.insert(ctk.END, message + "\n")
            self.progress_textbox.see(ctk.END)  # Scroll to the end
        self.lift()
        self.grab_set()

    def close(self,seconds=5000):
        self.after(seconds, self.destroy)
