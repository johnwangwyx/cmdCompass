import re
import os
from PIL import Image
import customtkinter as ctk
import sys

from pathlib import Path
import platform

IMG_DIR = "static"

def get_command_name(command_str):
    # Regular expression to match environment variables with optional quotes around the value
    env_var_pattern = r'\s*\w+=(".*?"|\'.*?\'|[^ ]*)\s*'

    # Remove all matched environment variable declarations
    cleaned_command = re.sub(env_var_pattern, '', command_str).strip()

    # Now split the remaining command by whitespace and return the first part
    parts = re.split(r'\s+', cleaned_command)
    if parts:
        return parts[0]
    raise ValueError(f"Unable to find the command name for {command_str}")


def get_current_working_dir():
    # Get the working dir when app is built as an executable.
    if getattr(sys, 'frozen', False) and platform.system() == "Darwin":
        # sys.executable in a PyInstaller bundle on macOS points to the MacOS executable
        # This resolves to MyApp.app/Contents/MacOS/MyApp.
        # So when user lick on Myapp.app, the real executable is 3 directory down.
        app_path = Path(sys.executable).resolve()
        # Navigate three levels up to get to the .app's parent directory
        application_root = app_path.parents[3]
    else:
        # If running as a normal script
        application_root = "."

    return application_root


def load_ctk_image(image_file_name, **kwargs):
    img_dir = os.path.join(get_current_working_dir(), IMG_DIR)
    image_path = os.path.join(img_dir, image_file_name)
    return ctk.CTkImage(light_image=Image.open(image_path), **kwargs)


def highlight_options(options, html, highlight_class="highlight"):
    highlighted_html = html

    highlighted_color = "yellow"
    if ctk.get_appearance_mode() == "Dark":
        highlighted_color = "red"

    for option in options:
        if len(option) == 1:
            # For single-letter options, match both '-' and '&minus;'
            pattern = r'([-&minus;]{})<'.format(re.escape(option))
            # Replace the pattern in the HTML with a highlighted version using <span> with inline style
            replacement = r'<span style="background-color:{};">\1</span><'.format(highlighted_color)
        else:
            # For multi-letter options, match both '--' and '&minus;&minus;' and handle hyphens in option names
            option_pattern = re.escape(option).replace('-', '[-&minus;]')
            pattern = r'([-&minus;][-&minus;]{})'.format(option_pattern)
            # Replace the pattern in the HTML with a highlighted version using <span> with inline style
            replacement = r'<span style="background-color:{};">\1</span>'.format(highlighted_color)

        highlighted_html = re.sub(pattern, replacement, highlighted_html)

    return highlighted_html
