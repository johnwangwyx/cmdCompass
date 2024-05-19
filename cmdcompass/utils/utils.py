import re
import os
import shutil

from PIL import Image
import customtkinter as ctk
import sys

from pathlib import Path
import platform
from platformdirs import PlatformDirs

APP_NAME = "CmdCompass"
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


def copy_resources(resource_name, source_root, dest_dir):
    source_path = source_root / resource_name
    dest_path = dest_dir / resource_name
    if not dest_path.exists():
        shutil.copytree(source_path, dest_path)
    return dest_path


def copy_data_and_static_to_app_support_dir():
    app_path = Path(sys.executable).resolve()
    resource_dir = Path(os.path.join(app_path.parents[1], "Resources"))

    # i.e /Users/<User>/Library/Application Support/<App>
    app_support_path = Path(get_data_and_static_parent_dir())
    app_support_path.mkdir(parents=True, exist_ok=True)

    # Copy 'data' and 'static' directories if they do not exist
    copy_resources('data', resource_dir, app_support_path)
    copy_resources('static', resource_dir, app_support_path)

def get_data_and_static_parent_dir():
    # Get the working dir when app is built as an executable.
    if getattr(sys, 'frozen', False) and platform.system() == "Darwin":
        dirs = PlatformDirs(appname=APP_NAME)
        # Use /Users/<User>/Library/Application Support/CmdCompass as the applications data and static root
        application_root = dirs.user_data_dir
    else:
        # If running as a normal script
        application_root = "."

    return application_root


def load_ctk_image(image_file_name, **kwargs):
    img_dir = os.path.join(get_data_and_static_parent_dir(), IMG_DIR)
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
