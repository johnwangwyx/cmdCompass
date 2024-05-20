import requests
import os
import gzip
import tarfile
import shutil
import arpy
import re
from sqlitedict import SqliteDict
from cmdcompass.man_parser.html_coverter import convert_man_pages
from cmdcompass.utils.utils import get_data_and_static_parent_dir
import platform
import sys

ARCH = "binary-amd64"
DEB_PACKAGE_URL = f"https://ftp.debian.org/debian/dists/Debian12.5/main/{ARCH}/Packages.gz"

if getattr(sys, 'frozen', False):
    BASE_DIR = get_data_and_static_parent_dir()
else:
    BASE_DIR = "."
UNPACKING_DIR = os.path.join(BASE_DIR, 'data', 'man_pages', 'tmp')
MAN_PAGE_DIR = os.path.join(BASE_DIR, 'data', 'man_pages', 'man')
KV_DB_PATH = os.path.join(BASE_DIR, 'data', 'man_pages_kv.db')

DEB_DOWNLOAD_LINK = "http://ftp.ca.debian.org/debian"


def extract_deb(data_path, extract_to):
    print(f"Extracting DEB package: {data_path} to {extract_to}")
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)
    # Open the DEB file as an AR archive
    with arpy.Archive(data_path) as archive:
        archive.read_all_headers()
        for name in archive.archived_files:
           if name.startswith(b'data.tar'):
                content = archive.archived_files[name]
                # Determine the compression based on the file extension
                if name.endswith(b'.gz'):
                    tar_mode = 'r:gz'
                elif name.endswith(b'.xz'):
                    tar_mode = 'r:xz'
                else:
                    tar_mode = 'r'
                
                # Write the data.tar content to a temporary file and extract
                tar_path = os.path.join(extract_to, name.decode())
                with open(tar_path, 'wb') as tar_file:
                    tar_file.write(content.read())

                # Extract the tar file using tarfile
                with tarfile.open(tar_path, mode=tar_mode) as tar:
                    tar.extractall(path=extract_to)

def download_file(url):
    print(f"Downloading file from {url}")
    local_filename = os.path.join(UNPACKING_DIR, url.split('/')[-1])
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

def extract_gz(file_path):
    print(f"Extracting gzip file {file_path}")
    with gzip.open(file_path, 'rb') as f:
        with open(file_path.replace('.gz', ''), 'wb') as f_out:
            f_out.write(f.read())

def move_and_clean_man_pages(package_name, extract_to, man_dest_folder):
    print(f"Scanning and moving man pages from {extract_to} to {man_dest_folder}")
    if platform.system() == 'Windows':
        man_page_regex = re.compile(r'(usr\\share\\man\\|usr\\man\\|usr\\X11R6\\man\\|usr\\local\\man/|opt\\man\\)')
    else:
        man_page_regex = re.compile(r"(usr/share/man/|usr/man/|usr/X11R6/man/|usr/local/man/|opt/man/)")

    # Ensure destination folder exists
    if not os.path.exists(man_dest_folder):
        os.makedirs(man_dest_folder)

    found_page = ""
    # Walk through the directory structure
    for root, dirs, files in os.walk(extract_to):
        # Check if current directory matches the man page directory pattern
        if not found_page and man_page_regex.search(root):
            for file in files:
                if file.endswith('.gz'):
                    src_file = os.path.join(root, file)
                    # Remove the .gz extension for the destination file
                    dst_file = os.path.join(man_dest_folder, file[:-3])  # Strip '.gz' from filename
                    # Not what we are looking for
                    if os.path.basename(dst_file).split('.')[0] != package_name:
                        continue
                    if not os.path.exists(dst_file):
                        # Decompress and move
                        with gzip.open(src_file, 'rb') as f_in:
                            with open(dst_file, 'wb') as f_out:
                                shutil.copyfileobj(f_in, f_out)
                        print(f"Decompressed and moved {src_file} to {dst_file}")
                        os.remove(src_file)
                        found_page = dst_file

    # Clean up the entire extracted directory structure
    shutil.rmtree(extract_to)
    print(f"Cleaned up extraction directory {extract_to}")
    return found_page

def download_and_process_package(package_name, progress_window):
    # Ensure destination folders exist
    if not os.path.exists(UNPACKING_DIR):
        os.makedirs(UNPACKING_DIR)
    with SqliteDict(KV_DB_PATH) as db:
        if package_name in db:
            try:
                # Note the db value can contain a list of package that includes the command man page.
                # The value is in tuple of ("package_link", #number of man pages in this package) and ordered by the #number
                # We can have a feature to allow user to choose which package to use
                # For now, I will just use the first tuple, which will result in a faster extraction
                link = db[package_name][0][0]  # Get package link from the first tuple
                full_link = f"{DEB_DOWNLOAD_LINK}/{link}"
                progress_window.update_progress(f"{package_name} is found in {link}.", 0.2)
                progress_window.update_progress(f"Downloading from {full_link}", 0.2)

                deb_path = download_file(full_link)
                progress_window.update_progress(f"Downloading completed.", 0.3)
                progress_window.update_progress(f"Unpacking and extracting man pages in this package...", 0.3)
                extract_to = os.path.join(UNPACKING_DIR, os.path.basename(deb_path).replace('.deb', ''))

                extract_deb(deb_path, extract_to)
                page_found = move_and_clean_man_pages(package_name, extract_to, MAN_PAGE_DIR)

                progress_window.update_progress(f"Converting the man for {package_name} to html", 0.7)
                if page_found:
                    progress_window.update_progress(f"Converting {page_found} to HTML...")
                    convert_man_pages(page_found)  # Convert only the matching page
                else:
                    progress_window.update_progress(f"No matching man page found for {package_name}")
                os.remove(deb_path)  # Remove the .deb file to free up space
            except Exception as e:
                progress_window.update_progress(f"Error: {e}")
        else:
            progress_window.update_progress(f"No download link found for package name: {package_name}")
            raise ValueError(f"No download link found for package name: {package_name}")
