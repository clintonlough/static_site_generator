from copystatic import copy_directory_contents_recursive
from generatepage import extract_title, generate_path
import shutil
import sys

def copy_static():
    #deletes the destination directory
    print("Deleting destination directory...")
    dest_dir = "./public"
    src_dir = "./static"
    shutil.rmtree(dest_dir)
    print("Copying static files to destination directory...")
    copy_directory_contents_recursive(src_dir, dest_dir)


def main():
    copy_static()
    from_path = "./content/index.md"
    template_path = "./template.html"
    dest_path = "./placeholder.txt"
    generate_path(from_path, template_path, dest_path)



main()