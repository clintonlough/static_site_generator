from copystatic import copy_directory_contents_recursive
from generatepage import generate_pages_recursive
import shutil
import os

def copy_static():
    #deletes the destination directory
    print("Deleting destination directory...")
    dest_dir = "./public"
    src_dir = "./static"
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    print("Copying static files to destination directory...")
    copy_directory_contents_recursive(src_dir, dest_dir)

def main():

    copy_static()

    dir_path_content = "./content"
    template_path = "./template.html"
    dest_dir_path = "./public"

    generate_pages_recursive(dir_path_content, template_path, dest_dir_path)



main()