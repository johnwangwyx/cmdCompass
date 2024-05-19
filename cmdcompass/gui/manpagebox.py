import customtkinter as ctk
from tkinterweb import HtmlFrame
import os
from cmdcompass.utils.utils import get_command_name, highlight_options, get_data_and_static_parent_dir
from cmdcompass.man_parser.loader import download_and_process_package
from cmdcompass.man_parser.html_coverter import OUTPUT_DIR
from cmdcompass.gui.progresswindow import ProgressWindow
from cmdcompass.gui.setmanpagewindow import SetManPageWindow
from tkinter import ttk
import sys
from sqlitedict import SqliteDict

if getattr(sys, 'frozen', False):
    BASE_DIR = get_data_and_static_parent_dir()
else:
    BASE_DIR = "."
HTML_CORE_DIR = os.path.join(BASE_DIR, 'data', 'man_pages', 'html_core')
DB_PATH = os.path.join(BASE_DIR, 'data', 'man_pages_kv.db')


class ManPageBox(ctk.CTkFrame):
    def __init__(self, master, main_window, **kwargs):
        super().__init__(master, **kwargs)
        self.main_window = main_window
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.html_view = HtmlFrame(self, height=370)
        self.html_view.grid(row=1, column=0, columnspan=2, sticky="nsew")
        self.html_view.grid_propagate(0)
        self.capture_original_scroll_bar_style()
        self.html_content = ""

        self.highlight_switch = ctk.CTkSwitch(self, text="Highlight My Options", command=self.apply_with_highlight)
        self.not_the_page_button = ctk.CTkButton(
            self,
            text="Not the right page?",
            command=lambda: self.open_set_man_page_window(),
            height=15
        )
        self.not_the_page_button.grid(row=0, column=1, pady=(5,0), sticky="w")

    def capture_original_scroll_bar_style(self):
        style = ttk.Style()
        self.original_config = {
            "gripcount": style.lookup("Vertical.TScrollbar", "gripcount"),
            "background": style.lookup("Vertical.TScrollbar", "background"),
            "darkcolor": style.lookup("Vertical.TScrollbar", "darkcolor"),
            "lightcolor": style.lookup("Vertical.TScrollbar", "lightcolor"),
            "troughcolor": style.lookup("Vertical.TScrollbar", "troughcolor"),
            "bordercolor": style.lookup("Vertical.TScrollbar", "bordercolor"),
            "arrowcolor": style.lookup("Vertical.TScrollbar", "arrowcolor")
        }

    def set_man_page(self, command):
        html_content = ""
        self.command = command
        command_str = command.command_str
        if command.user_defined_man_page :
            command_str = command.user_defined_man_page
        try:
            command_name = get_command_name(command_str)

            dynamically_downloaded_html = os.path.join(OUTPUT_DIR, f"{command_name}.html")
            existing_core_man_page = os.path.join(HTML_CORE_DIR, f"{command_name}.html")
            if os.path.exists(existing_core_man_page):
                with open(existing_core_man_page, "r") as f:
                    html_content = f.read()
            elif os.path.exists(dynamically_downloaded_html):
                with open(dynamically_downloaded_html, "r") as f:
                    html_content = f.read()
            else:
                def download_and_update():
                    progress_window = self.create_progress_window()
                    progress_window.update_progress(HTML_CORE_DIR)
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
        self.html_content = html_content
        self.options = command.extract_options()
        self.change_theme()
        if self.options:
            self.highlight_switch.grid(row=0, column=0, pady=(10, 0), sticky="w")
        else:
            self.highlight_switch.grid_forget()

    def create_progress_window(self):
        progress_window = ProgressWindow(self.master, "Man Pages Processing")
        return progress_window

    def change_theme(self):
        style = ttk.Style()
        if ctk.get_appearance_mode() == "Dark":
            style.theme_use('clam')
            style.configure("Vertical.TScrollbar", gripcount=0,
                            background="black", darkcolor="grey", lightcolor="grey",
                            troughcolor="black", bordercolor="black", arrowcolor="grey")
            self.html_view.enable_dark_theme(enabled=True, invert_images=False)
        else:
            style.configure("Vertical.TScrollbar", **self.original_config)
            self.html_view.enable_dark_theme(enabled=False, invert_images=False)
        self.apply_with_highlight()

    def apply_with_highlight(self):
        html_content = self.html_content
        if self.highlight_switch.get() == 1:
            html_content = highlight_options(self.options, self.html_content)
        self.html_view.load_html(html_content)

    def open_set_man_page_window(self):
        set_man_page_window = SetManPageWindow(self, self.command, self.main_window)
        command_name = get_command_name(self.command.command_str)

        suggestion = []
        with SqliteDict(DB_PATH) as db:
            for command in db:
                if command.startswith(command_name):
                    suggestion.append(command)
        suggestion.sort()

        set_man_page_window.set_suggestions(suggestion)