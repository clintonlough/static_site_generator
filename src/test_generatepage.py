import unittest

from generatepage import extract_title

class TestGeneratePage(unittest.TestCase):
    def test_title_extract(self):
        markdown = ['# Tolkien Fan Club\n', '\n', '![JRR Tolkien sitting](/images/tolkien.png)\n']
        self.assertEqual(extract_title(markdown), "Tolkien Fan Club")

    def test_title_extract_whitespace(self):
        markdown = ['#    Tolkien Fan Club   \n', '\n', '![JRR Tolkien sitting](/images/tolkien.png)\n']
        self.assertEqual(extract_title(markdown), "Tolkien Fan Club")

    def test_no_title_extract(self):
        markdown = ['![JRR Tolkien sitting](/images/tolkien.png)\n']
        with self.assertRaises(ValueError) as context:
            extract_title(markdown)
        self.assertIn("Heading not found in file", str(context.exception))

if __name__ == "__main__":
    unittest.main()