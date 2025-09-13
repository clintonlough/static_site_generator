from copystatic import copy_directory_contents_recursive
from generatepage import generate_pages_recursive
import shutil
import os
import sys

def copy_static(dest_dir_path):
    #deletes the destination directory
    print("Deleting destination directory...") 
    src_dir = "./static"
    if os.path.exists(dest_dir_path):
        shutil.rmtree(dest_dir_path)
    print("Copying static files to destination directory...")
    copy_directory_contents_recursive(src_dir, dest_dir_path)

def main():

    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else: 
        basepath = "/"

    print(basepath)
    dir_path_content = "./content"
    template_path = "./template.html"
    dest_dir_path = "./docs"

    copy_static(dest_dir_path)
    generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath)



main()