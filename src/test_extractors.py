import unittest

from extractors import extract_markdown_images, extract_markdown_links

class TestExtractors(unittest.TestCase):
    def test_extract_markdown_images(self):
        actual = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], actual)

    def test_extract_markdown_links(self):
        actual = extract_markdown_links(
            text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev'),], actual)