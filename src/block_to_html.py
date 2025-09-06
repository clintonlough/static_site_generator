from textnode import *
from htmlnode import *
from block_markdown import *
from inline import *
import re
import textwrap

#Takes a block and converts it into the correct HTML Node
def block_to_html_node(block, block_type):
    match block_type:
        case BlockType.HEADING:
            print("this is a heading")
            node = HTMLNode(tag = "h", value = block, children = None, props = None):
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