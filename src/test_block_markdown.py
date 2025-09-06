import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

    def test_markdown_to_blocks_multiline(self):
            md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

    def test_block_type_ordered_list(self):
        markdown = """1. this is a quote
    2. this is the 2nd line
    3. this is the 3rd"""
        self.assertEqual(BlockType.ORDERED_LIST,block_to_block_type(markdown))

    def test_block_type_code(self):
          markdown = "``` this is a code block ```"
          self.assertEqual(BlockType.CODE,block_to_block_type(markdown))

    def test_block_type_unordered_list(self):
          markdown = """
            - this is an ordered list
            - this is item 2
            this is item 3
          """
          self.assertEqual(BlockType.UNORDERED_LIST,block_to_block_type(markdown))

    def test_block_type_quote(self):
          markdown = """
        > to be or not to be
        > that is the question
        """
          self.assertEqual(BlockType.QUOTE,block_to_block_type(markdown))

    def test_block_type_paragraph(self):
        markdown = """
        this is just a random paragraph
        with a few lines of text
        - and a list item
        """
        self.assertEqual(BlockType.PARAGRAPH,block_to_block_type(markdown))