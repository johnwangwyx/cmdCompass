import re
import os
from PIL import Image
import customtkinter as ctk

IMG_DIR = os.path.join(".", "static")

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


def load_ctk_image(image_file_name, **kwargs):
    image_path = os.path.join(IMG_DIR, image_file_name)
    return ctk.CTkImage(light_image=Image.open(image_path), **kwargs)


def highlight_options(options, html, highlight_class="highlight"):
    highlighted_html = html

    highlighted_color = "yellow"
    if ctk.get_appearance_mode() == "Dark":
        highlighted_color = "red"

    for option in options:
        if len(option) == 1:
            # For single-letter options, expect them to be followed by a specific character like "<"
            pattern = r'(-{})<'.format(re.escape(option))
            # Replace the pattern in the HTML with a highlighted version using <span> with inline style
            replacement = r'<span style="background-color:{};">\1</span><'.format(highlighted_color)
        else:
            # For multi-letter options, just match the option itself with "--"
            pattern = r'(--{})'.format(re.escape(option))
            # Replace the pattern in the HTML with a highlighted version using <span> with inline style
            replacement = r'<span style="background-color:{};">\1</span>'.format(highlighted_color)

        highlighted_html = re.sub(pattern, replacement, highlighted_html)

    return highlighted_html

