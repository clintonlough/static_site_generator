from block_markdown import markdown_to_html_node
from htmlnode import ParentNode
import os

def extract_title(markdown_lines):
    heading = None
    for line in markdown_lines:
        if line.startswith("# "):
            heading = line[2:].strip()
    if heading == None:
        raise ValueError("Heading not found in file")
    print(f"heading is {heading}")
    return heading

def create_directories(dest_path):
    file_path = os.path.dirname(dest_path)
    print(file_path)
    os.makedirs(file_path, mode=0o777, exist_ok=True)



def generate_path(from_path, template_path, dest_path):
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

    #Write the html file to a destination file
    create_directories(dest_path)
    dest_file = open(dest_path, mode='w')
    dest_file.write(template_contents)
    dest_file.close()