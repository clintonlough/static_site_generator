import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_htmlnode(self):
        # Link Test
        node1 = HTMLNode("a", "Click me", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node1.props_to_html(), ' href="https://www.google.com" target="_blank"')
                        
        # Paragraph test with no props or children
        node2 = HTMLNode("p", "Hello world")
        self.assertEqual(node2.props_to_html(), "")

        #Tests __repr__ method
        expected = "HTMLNode(a, Click me, children: None, {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual(str(node1), expected)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_empty_parents(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_to_html_nested_parents(self):
        parent_node = ParentNode("div", [])
        parent_node2 = ParentNode("div",[parent_node])
        self.assertEqual(parent_node2.to_html(), "<div><div></div></div>")

if __name__ == "__main__":
    unittest.main()