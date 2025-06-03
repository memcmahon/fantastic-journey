import unittest

from textnode import TextNode, TextType

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

if __name__ == "__main__":
    unittest.main()