import customtkinter as ctk
from tkinterweb import HtmlFrame
import os
from cmdcompass.utils.utils import get_command_name
from cmdcompass.man_parser.loader import download_and_process_package
from cmdcompass.man_parser.html_coverter import OUTPUT_DIR
from cmdcompass.gui.progresswindow import ProgressWindow

HTML_CORE_DIR = "./data/man_pages/html_core"

class ManPageBox(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.html_view = HtmlFrame(self, height=450)
        self.html_view.pack(fill="both", expand=True)
        self.html_view.grid_propagate(0)

    def set_man_page(self, command_str):
        html_content = ""
        try:
            command_name = get_command_name(command_str)

            dynamically_downloaded_html = f"{OUTPUT_DIR}/{command_name}.html"
            existing_core_man_page = f"{HTML_CORE_DIR}/{command_name}.html"
            if os.path.exists(existing_core_man_page):
                with open(existing_core_man_page, "r") as f:
                    html_content = f.read()
            elif os.path.exists(dynamically_downloaded_html):
                with open(dynamically_downloaded_html, "r") as f:
                    html_content = f.read()
            else:
                def download_and_update():
                    progress_window = self.create_progress_window()
                    progress_window.update_progress(f"Downloading {command_name}...")
                    download_and_process_package(command_name, progress_window)
                    # After download and processing is complete, update the HTML
                    with open(dynamically_downloaded_html, "r") as f:
                        html_content = f.read()
                    self.html_view.load_html(html_content)
                    if progress_window:
                        progress_window.update_progress("Complete! Closing Window in 5 seconds", 1)
                        progress_window.close()

                # Create and start a new thread for downloading and processing
                import threading
                download_thread = threading.Thread(target=download_and_update)
                download_thread.start()
        except Exception as e:
            print(f"Error getting man page: {e}")
        self.html_view.load_html(html_content)

    def create_progress_window(self):
        progress_window = ProgressWindow(self.master, "Man Pages Processing")
        return progress_window


