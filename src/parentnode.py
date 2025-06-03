from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag = tag, children = children, props = props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("tag is required")
        if self.children is None or len(self.children) == 0:
            raise ValueError("parent must have children")
        result = ""
        for child in self.children:
            result += child.to_html()
        if self.props is None:
            return f"<{self.tag}>{result}</{self.tag}>"
        return f"<{self.tag}{self.props}>{result}</{self.tag}>"