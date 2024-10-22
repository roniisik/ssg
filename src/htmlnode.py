  
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = ""
        if self.props == None:
            return result
        for prop in self.props:
            result += f' {prop}="{self.props[prop]}"'
        
        return result
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def __eq__(self, other):
        if isinstance(other, HTMLNode):
            return (self.tag == other.tag and
                    self.value == other.value and
                    self.children == other.children and
                    self.props == other.props)
        else:
            return False
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.children}, {self.props})"
        
    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode has no value")
        
        if self.tag == None:
            return self.value
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode has no tag")
        
        if self.children == None or self.children == False:
            raise ValueError("ParentNode has no children")
        else:
            result = f"<{self.tag}{self.props_to_html()}>"
            for node in self.children:
                result += node.to_html()
            
            return result + "</" + self.tag + ">"
        

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
    
