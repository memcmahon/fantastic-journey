import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        html_node1 = HTMLNode()
        html_node2 = HTMLNode(value="This is a html node")
        html_node3 = HTMLNode(children=[html_node1, html_node2])
        html_node4 = HTMLNode(tag = "a", value = "This is a link", props = {"href": "https://turing.edu"})
        for node in [html_node1, html_node2, html_node3, html_node4]:
            self.assertIsInstance(node, HTMLNode)
    
    def test_props_to_html(self):
        html_node1 = HTMLNode()
        html_node4 = HTMLNode(tag = "a", value = "This is a link", props = {"href": "https://turing.edu"})
        self.assertEqual(html_node4.props_to_html(), " href=\"https://turing.edu\"")
        self.assertEqual(html_node1.props_to_html(), "")
    
    def test_repr(self):
        html_node4 = HTMLNode(tag = "a", value = "This is a link", props = {"href": "https://turing.edu"})
        self.assertEqual(repr(html_node4), "HTMLNode: a This is a link None {'href': 'https://turing.edu'}")