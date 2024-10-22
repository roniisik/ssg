import unittest
from node_funcs import *
import textnode

class TestRegex(unittest.TestCase):
    def test_extract_markdown_links(self):
        text = "This is a link [Link to bomba](https://www.boot.dev/lessons/ab12db79-fc4e-46f1-81d2-4694e7f3b8f6) and [Link to Scholmba](https://chatgpt.com/c/66fdb218-254c-8011-adb7-7d18f561a182) and [ link to blumpi](http://localhost:8888/)"
        expected_result = [("Link to bomba", "https://www.boot.dev/lessons/ab12db79-fc4e-46f1-81d2-4694e7f3b8f6"), ("Link to Scholmba", "https://chatgpt.com/c/66fdb218-254c-8011-adb7-7d18f561a182"), (" link to blumpi", "http://localhost:8888/")]
        self.assertEqual(expected_result, extract_markdown_links(text))

    def test_extract_markdown_images(self):
        text = "This is a link [Link to bomba](https://www.boot.dev/lessons/ab12db79-fc4e-46f1-81d2-4694e7f3b8f6) and [Link to Scholmba](https://chatgpt.com/c/66fdb218-254c-8011-adb7-7d18f561a182) and [ link to blumpi](http://localhost:8888/)"
        expected_result = [("Link to bomba", "https://www.boot.dev/lessons/ab12db79-fc4e-46f1-81d2-4694e7f3b8f6"), ("Link to Scholmba", "https://chatgpt.com/c/66fdb218-254c-8011-adb7-7d18f561a182"), (" link to blumpi", "http://localhost:8888/")]
        self.assertEqual(expected_result, extract_markdown_links(text))

    def test_extract_markdown_links_textnode(self):
        text_node = TextNode("Hello [Link test](http:linkto.bomba.com)", TextType.TEXT)
        expected_result = [("Link test", "http:linkto.bomba.com")]
        self.assertEqual(expected_result, extract_markdown_links(text_node.text))

    def test_extract_markdown_images_nourl(self):
        text = "Hello [Link test]Hello"
        expected_result = []
        self.assertEqual(expected_result, extract_markdown_links(text))

    def test_extract_markdown_images_noalt(self):
        text = "Hello (http:linkto.bomba.com)"
        expected_result = []
        self.assertEqual(expected_result, extract_markdown_links(text))

class TestBlockFuncs(unittest.TestCase):
    pass
