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
