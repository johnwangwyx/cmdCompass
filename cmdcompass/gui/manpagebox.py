import customtkinter as ctk
from tkinterweb import HtmlFrame
import os
from cmdcompass.utils.utils import get_command_name
from cmdcompass.man_parser.loader import download_and_process_package
from cmdcompass.man_parser.html_coverter import OUTPUT_DIR

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

            html_file = f"{OUTPUT_DIR}/{command_name}.html"
            existing_man_page = f"{HTML_CORE_DIR}/{command_name}.html"
            if os.path.exists(html_file):
                with open(html_file, "r") as f:
                    html_content = f.read()
            if os.path.exists(existing_man_page):
                with open(existing_man_page, "r") as f:
                    html_content = f.read()
            download_and_process_package(command_name)
        except Exception as e:
            print(f"Error getting man page: {e}")
        self.html_view.load_html(html_content)

