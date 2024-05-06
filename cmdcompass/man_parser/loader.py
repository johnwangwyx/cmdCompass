import requests
import os
import gzip
import tarfile
import shutil
import arpy
import re
from sqlitedict import SqliteDict
from  cmdcompass.man_parser.html_coverter import convert_man_pages

ARCH = "binary-amd64"
DEB_PACKAGE_URL = f"https://ftp.debian.org/debian/dists/Debian12.5/main/{ARCH}/Packages.gz"
UNPACKING_DIR = "./data/man_pages/tmp"
MAN_PAGE_DIR = "./data/man_pages/man"
KV_DB_PATH = "./man_parser/man_pages_kv.db"
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
    local_filename = url.split('/')[-1]
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

def move_and_clean_man_pages(extract_to, man_dest_folder):
    print(f"Scanning and moving man pages from {extract_to} to {man_dest_folder}")
    man_page_regex = re.compile(r'(usr\\share\\man\\|usr\\man\\|usr\\X11R6\\man\\|usr\\local\\man/|opt\\man\\)')

    pages_found = []
    
    # Ensure destination folder exists
    if not os.path.exists(man_dest_folder):
        os.makedirs(man_dest_folder)
    
    # Walk through the directory structure
    for root, dirs, files in os.walk(extract_to):
        # Check if current directory matches the man page directory pattern
        if man_page_regex.search(root):
            for file in files:
                if file.endswith('.gz'):
                    src_file = os.path.join(root, file)
                    # Remove the .gz extension for the destination file
                    dst_file = os.path.join(man_dest_folder, file[:-3])  # Strip '.gz' from filename
                    pages_found.append(dst_file)
     
                    if not os.path.exists(dst_file):
                        # Decompress and move
                        with gzip.open(src_file, 'rb') as f_in:
                            with open(dst_file, 'wb') as f_out:
                                shutil.copyfileobj(f_in, f_out)
                        print(f"Decompressed and moved {src_file} to {dst_file}")
                        os.remove(src_file)
                    else:
                        print(f"File {dst_file} already exists. Skipping.")

    # Clean up the entire extracted directory structure
    shutil.rmtree(extract_to)
    print(f"Cleaned up extraction directory {extract_to}")
    return pages_found

def download_and_process_package(package_name):
    # Ensure destination folders exist
    if not os.path.exists(UNPACKING_DIR):
        os.makedirs(UNPACKING_DIR)
    
    with SqliteDict(KV_DB_PATH) as db:
        if package_name in db:
            link = db[package_name]
            full_link = f"{DEB_DOWNLOAD_LINK}/{link}"
            deb_path = download_file(full_link)
            extract_to = os.path.join(UNPACKING_DIR, os.path.basename(deb_path).replace('.deb', ''))
            extract_deb(deb_path, extract_to)
            pages_found = move_and_clean_man_pages(extract_to, MAN_PAGE_DIR)
            for man_page in pages_found:
                convert_man_pages(man_page)
            os.remove(deb_path)  # Remove the .deb file to free up space
        else:
            raise ValueError(f"No download link found for package name: {package_name}")
