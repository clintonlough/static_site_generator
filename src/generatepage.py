from block_markdown import markdown_to_html_node
from htmlnode import ParentNode
import os
import shutil

def extract_title(markdown_lines):
    heading = None
    for line in markdown_lines:
        if line.startswith("# "):
            heading = line[2:].strip()
    if heading == None:
        raise ValueError("Heading not found in file")
    return heading

def create_directories(dest_path):
    file_path = os.path.dirname(dest_path)
    os.makedirs(file_path, mode=0o777, exist_ok=True)


def generate_path(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    #markdown_file = f"{from_path}"
    markdown_file = open(from_path, mode='r')
    markdown = markdown_file.read()
    markdown_lines = markdown.splitlines()
    markdown_file.close()

    template_file = open(template_path, mode='r')
    template_contents = template_file.read()
    template_file.close()

    #Convert the markdown file to a HTML string
    parent_node = markdown_to_html_node(markdown)
    html_string = parent_node.to_html()
    title = extract_title(markdown_lines)

    template_contents = template_contents.replace("{{ Title }}",title)
    template_contents = template_contents.replace("{{ Content }}",html_string)

    #set the basepath for hosting
    template_contents = template_contents.replace('href="/', 'href="{basepath}')
    template_contents = template_contents.replace('src="/', 'src="{basepath}')

    #Write the html file to a destination file
    create_directories(dest_path)
    if dest_path.endswith(".md"):
        dest_path = dest_path.replace(".md",".html")
    dest_file = open(dest_path, mode='w')
    dest_file.write(template_contents)
    dest_file.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    items_to_copy = os.listdir(path=dir_path_content)
    print(items_to_copy)

    if not os.path.exists(dir_path_content):
        os.mkdir(dir_path_content)
    for filename in os.listdir(path=dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            generate_path(from_path,template_path, dest_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)