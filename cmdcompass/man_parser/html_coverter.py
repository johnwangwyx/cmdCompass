import os
import subprocess
import platform

WINDOWS_GROFF_BIN = "./man_parser/bin/groff-1.22.4-w32-bin/bin/groff.exe"
OUTPUT_DIR = "./data/man_pages/html"


def convert_man_pages(man_file, output_dir=OUTPUT_DIR):
    # Ensure destination folder exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Determine the appropriate groff command based on the OS
    # MAC and Linux should have native support for groff. For Windows a pre-build binary need to be used.
    if platform.system() == 'Windows':
        groff_command = [WINDOWS_GROFF_BIN, '-mandoc', '-Thtml', man_file]
    else:
        groff_command = ['groff', '-mandoc', '-Thtml', man_file]

    base_name = os.path.basename(man_file)  # Get the file name without the directory path
    name_without_ext = os.path.splitext(base_name)[0]  # Remove extension
    output_path = os.path.join(output_dir, name_without_ext + '.html')
    if not os.path.exists(output_path):
        with open(output_path, 'w') as outfile:
            subprocess.run(groff_command, stdout=outfile)
    else:
        print(f"File {output_path} already exists. Skipping.")