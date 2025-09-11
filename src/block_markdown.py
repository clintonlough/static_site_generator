from textnode import TextType, TextNode, text_node_to_html_node
from htmlnode import HTMLNode, ParentNode, LeafNode
from inline import text_to_textnodes
import re
from enum import Enum
import textwrap

BlockType = Enum("Block_Type", ['PARAGRAPH', 'HEADING', 'CODE', 'QUOTE', 'UNORDERED_LIST', 'ORDERED_LIST'])

def markdown_to_blocks(markdown):
    # Remove common test indent and trim outer newlines
    markdown = textwrap.dedent(markdown).strip("\n")

    # Normalise newlines (optional, helps on Windows inputs)
    markdown = markdown.replace("\r\n", "\n").replace("\r", "\n")

    # Split on 1+ blank lines (which may contain spaces/tabs)
    blocks = re.split(r"\n[ \t]*\n+", markdown)

    # Keep internal newlines, just trim spaces/tabs at block edges
    blocks = [b.strip(" \t") for b in blocks if b.strip(" \t")]

    return blocks

#Checks that each line of a block is an ordered list item in order.
def check_ordered_list(block):
    lines = block.splitlines()
    i = 1
    match = False
    for line in lines:
        pattern = rf"^\s*{i}\. "
        match = re.match(pattern, line)
        if not match:
            return False
        i += 1
    return True

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1:]
    children = text_to_children(text)
    return ParentNode(f"h{level}",children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def ul_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def ol_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def block_to_block_type(block):
    #Heading must start with 1 - 6 #s
    if re.match(r"^#{1,6}(?!#)", block):
        return BlockType.HEADING
    #Code blocks must start and end with 3 x ```
    elif re.match(r"^`{3}[\s\S]*`{3}$", block, flags=re.DOTALL):
        return BlockType.CODE
    #Quote lines start with a >
    elif re.match(r"^\s*\>", block, flags=re.MULTILINE):
        return BlockType.QUOTE
    # Unordered list: any line starting with "- "
    elif re.match(r"^\s*\- ", block, flags=re.MULTILINE):
        return BlockType.UNORDERED_LIST
    #check each line is an incrementing ordered list
    elif check_ordered_list(block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

#Takes a block and converts it into the correct HTML Node
def block_to_html_node(block):
    block_type = block_to_block_type(block)
    match block_type:
        case BlockType.HEADING:
            return heading_to_html_node(block)
        case BlockType.CODE:
            return code_to_html_node(block)
        case BlockType.QUOTE:
            return quote_to_html_node(block)
        case BlockType.UNORDERED_LIST:
            return ul_to_html_node(block)
        case BlockType.ORDERED_LIST:
            return ol_to_html_node(block)
        case BlockType.PARAGRAPH:
            return paragraph_to_html_node(block)
    return


def markdown_to_html_node(markdown):
    #split markdown into blocks
    blocks = markdown_to_blocks(markdown)
    children= []
    # loop over each block
    for block in blocks:
        #create HTMLNode
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

def main():
    markdown = """
### This is the heading


1. this is an order
2. list
3. of 3 items


> and this is a quote
> about cows


This is just a random paragraph


"""

    parent = markdown_to_html_node(markdown)

main()