import unittest
from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props_tohtml(self):
        node = HTMLNode(props={"href": "bomba.com", "src": "source"})
        
        self.assertEqual(f' href="bomba.com" src="source"', node.props_to_html())

    def test_empty_props(self):
        node = HTMLNode(props={})
        self.assertEqual(f'', node.props_to_html())

    def test_one_props(self):
        node = HTMLNode(props={"href": "bomba.com"})
        self.assertEqual(f' href="bomba.com"', node.props_to_html())

    def test_leafto_html_full(self):
        node = LeafNode("a", "Bombastic!", props={"href": "bomba.com", "src": "source.com"})
        self.assertEqual(node.to_html(), '<a href="bomba.com" src="source.com">Bombastic!</a>')

    """ def test_leafto_html_noval(self):
        node = LeafNode(tag="a", value=None, props={"href": "bomba.com"})
        self.assertEqual(node.to_html(), ValueError) """

    def test_leafto_html_notag(self):
        node = LeafNode(tag=None, value="Bombastic!", props={"href": "bomba.com"})
        self.assertEqual(node.to_html(), "Bombastic!")

    def test_parentto_html_oneleaf(self):
        node = ParentNode(tag="p", children=[LeafNode(tag="b", value="Bomb")])
        self.assertEqual(node.to_html(), '<p><b>Bomb</b></p>')

    def test_parentto_html_oneparent(self):
        node = ParentNode(tag="p", 
                          children=[ParentNode(tag="x", children=[LeafNode(value="Bombi")])])
        self.assertEqual(node.to_html(), '<p><x>Bombi</x></p>')

    def test_parentto_html_props(self):
        node = ParentNode(tag="p", 
                          children=[ParentNode(tag="x", children=[LeafNode(value="Bombi")], props={"bomb": "astic!", "pumb": "timon"})])
        self.assertEqual(node.to_html(), '<p><x bomb="astic!" pumb="timon">Bombi</x></p>')

    
    

    