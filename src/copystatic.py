import os
import shutil

def copy_directory_contents_recursive(src_dir, dest_dir):

    #All of this could be done with shutil.copytree() but lesson wants recursive
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    for filename in os.listdir(src_dir):
        from_path = os.path.join(src_dir, filename)
        dest_path = os.path.join(dest_dir, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_directory_contents_recursive(from_path, dest_path)