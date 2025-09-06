from textnode import TextType, TextNode
import re

# Takes a list of text nodes and splits them into new nodes of specific types based on markdown
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

#Takes a text string with one or more images and splits into new nodes.
def split_nodes_image(old_nodes):
        new_nodes = []
        #If not a text node then simply append to new_nodes and continue
        for node in old_nodes:
            if node.text_type != TextType.TEXT:
                new_nodes.append(node)
                continue
            #extract images using markdown function
            images = extract_markdown_images(node.text)
            #if not an image just append and continue
            if not images:
                new_nodes.append(node)
                continue
            #splits with partition and works its way through the whole string creating new nodes    
            remaining = node.text
            for alt, url in images:
                before, _, after = remaining.partition(f"![{alt}]({url})")
                if before:
                    new_nodes.append(TextNode(before,TextType.TEXT))
                new_nodes.append(TextNode(alt, TextType.IMAGE, url))
                remaining = after
            
            if remaining:
                new_nodes.append(TextNode(remaining,TextType.TEXT))

        return new_nodes

#Takes a text string with one or more links and splits into new nodes
def split_nodes_link(old_nodes):
    new_nodes = []
    #If not a text node then simply append to new_nodes and continue
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        #extract links using markdown function
        links = extract_markdown_links(node.text)
        #if not a link just append and continue
        if not links:
            new_nodes.append(node)
            continue
        #splits with partition and works its way through the whole string creating new nodes    
        remaining = node.text
        for text, url in links:
            before, _, after = remaining.partition(f"[{text}]({url})")
            if before:
                new_nodes.append(TextNode(before,TextType.TEXT))
            new_nodes.append(TextNode(text, TextType.LINK, url))
            remaining = after
        
        if remaining:
            new_nodes.append(TextNode(remaining,TextType.TEXT))

    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

#Example from Boot.Dev solution - much cleaner but confusing as fuck
def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def text_to_textnodes(text):
    old_node = TextNode(text, TextType.TEXT)
    code_nodes = split_nodes_delimiter([old_node],"`",TextType.CODE)
    bold_nodes = split_nodes_delimiter(code_nodes,"**",TextType.BOLD)
    italic_nodes = split_nodes_delimiter(bold_nodes,"_",TextType.ITALIC)
    image_nodes = split_nodes_image(italic_nodes)
    link_nodes = split_nodes_link(image_nodes)
    return link_nodes

def main():
    pass

main()