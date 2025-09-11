from textnode import TextType, TextNode
from htmlnode import HTMLNode
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
def block_to_html_node(block, block_type):
    match block_type:
        case BlockType.HEADING:
            print("this is a heading")
            node = HTMLNode(tag = "h", value = block, children = None, props = None)
        case BlockType.CODE:
            pass
        case BlockType.QUOTE:
            print("this is a quote")
        case BlockType.UNORDERED_LIST:
            pass
        case BlockType.ORDERED_LIST:
            print("this is an ordered list")
        case BlockType.PARAGRAPH:
            print("this is a paragraph")
    return


def markdown_to_html_node(markdown):
    #split markdown into blocks
    blocks = markdown_to_blocks(markdown)
    # loop over each block
    for block in blocks:
        #determine block type
        block_type = block_to_block_type(block)
        #create HTMLNode
        html_node = block_to_html_node(block, block_type)
        #Assign children HTMLNodes to the block - use a helper
    
    #make all the block nodes children under a single parent HTML Node (Div) and return it
    return


def main():
    markdown = """
###This is the heading


1. this is an order
2. list
3. of 3 items


> and this is a quote
> about cows


This is just a random paragraph


"""

    markdown_to_html_node(markdown)

main()