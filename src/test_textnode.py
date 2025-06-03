import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    # init
    def test_init(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a image node", TextType.IMAGE, "http://test.com")
        self.assertRaises(ValueError, lambda: TextNode("This is not a node", "happy", "http://test.com"))
        self.assertIsInstance(node1, TextNode)
        self.assertIsInstance(node2, TextNode)

    # eq
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a kind of node", TextType.BOLD)
        self.assertEqual(node1, node2)
        self.assertNotEqual(node2, node3)

    # repr
    def test_repr(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a image node", TextType.IMAGE, "http://test.com")
        self.assertEqual(repr(node1), "TextNode(This is a text node, bold, None)")
        self.assertEqual(repr(node2), "TextNode(This is a image node, image, http://test.com)")

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()