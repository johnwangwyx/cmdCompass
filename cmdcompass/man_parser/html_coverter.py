import os
import subprocess
import platform
import sys
from cmdcompass.utils.utils import get_data_and_static_parent_dir
import shutil
from pathlib import Path

if getattr(sys, 'frozen', False):
    BASE_DIR = get_data_and_static_parent_dir()
else:
    BASE_DIR = "."
WINDOWS_GROFF_BIN = os.path.join(BASE_DIR, 'data', 'bin', 'groff-1.22.4-w32-bin', 'bin', 'groff.exe')
OUTPUT_DIR = os.path.join(BASE_DIR, 'data', 'man_pages', 'html_download')
CREATE_NO_WINDOW = 0x08000000  # To used on Windows to not open any terminal window while using subprocess

def convert_man_pages(man_file, output_dir=OUTPUT_DIR):
    # Ensure destination folder exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Determine the appropriate groff command based on the OS
    # MAC and Linux should have native support for groff. For Windows a pre-build binary need to be used.
    if platform.system() == 'Windows':
        groff_command = [WINDOWS_GROFF_BIN, '-mandoc', '-Thtml', man_file]
    else:
        # Try to locate 'groff' using 'which' command
        # As per https://pyinstaller.org/en/stable/common-issues-and-pitfalls.html#macos,
        # If the app is run from Finder, the app may have a reduced set of PATH vars, which may not include groff
        groff_path = shutil.which('groff')
        if not groff_path:
            # Fallback to common paths if not found
            for path in ['/usr/local/bin/groff', '/opt/homebrew/bin/groff']:
                if Path(path).exists():
                    groff_path = path
                    break
        if groff_path is None:
            raise FileNotFoundError("The 'groff' command is not available in the system PATH.")
        groff_command = [groff_path, '-mandoc', '-Thtml', man_file]

    base_name = os.path.basename(man_file)  # Get the file name without the directory path
    name_without_ext = os.path.splitext(base_name)[0]  # Remove extension
    output_path = os.path.join(output_dir, name_without_ext + '.html')
    if not os.path.exists(output_path):
        with open(output_path, 'w') as outfile:
            if platform.system() == 'Windows':
                subprocess.run(groff_command, stdout=outfile, creationflags=CREATE_NO_WINDOW)
            else:
                subprocess.run(groff_command, stdout=outfile)
    else:
        print(f"File {output_path} already exists. Skipping.")