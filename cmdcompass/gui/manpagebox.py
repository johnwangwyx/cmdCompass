import customtkinter as ctk
import tkhtmlview
import os
from cmdcompass.utils.utils import get_command_name
from cmdcompass.man_parser.loader import download_and_process_package
from cmdcompass.man_parser.html_coverter import OUTPUT_DIR


class ManPageBox(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.html_view = tkhtmlview.HTMLLabel(self)
        self.html_view.pack(fill="both", expand=True)

    def set_man_page(self, command_str):
        html_content = ""
        try:
            command_name = get_command_name(command_str)
            html_file = f"{OUTPUT_DIR}/{command_name}.html"

            if not os.path.exists(html_file):
                download_and_process_package(command_name)

            if os.path.exists(html_file):
                with open(html_file, "r") as f:
                    html_content = f.read()
        except Exception as e:
            print(f"Error getting man page: {e}")
        self.html_view.set_html(html_content)

