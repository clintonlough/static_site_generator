from block_markdown import markdown_to_html_node
from htmlnode import ParentNode

def extract_title(markdown_lines):
    heading = None
    for line in markdown_lines:
        if line.startswith("# "):
            heading = line[2:].strip()
    if heading == None:
        raise ValueError("Heading not found in file")
    print(f"heading is {heading}")
    return heading

def generate_path(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown_file = f"{from_path}"
    markdown_file_r = open(markdown_file, mode='r')
    markdown = markdown_file_r.read()
    markdown_lines = markdown.splitlines()
    template_file = f"{template_path}"
    template_file_r = open(template_file, mode='r')
    template_contents = template_file_r.read()

    #Convert the markdown file to a HTML string
    parent_node = markdown_to_html_node(markdown)
    html_string = parent_node.to_html()
    title = extract_title(markdown_lines)

    template_contents = template_contents.replace("{{ Title }}",title)
    #template_contents = template_contents.replace("{{ Content }}",html_string)

    #print(template_contents)