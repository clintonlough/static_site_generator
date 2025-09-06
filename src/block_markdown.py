from textnode import TextType, TextNode
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

def main():
    pass

main()