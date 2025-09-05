class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props:
            prop_str = ""
            for k, v in self.props.items():
                prop_str += " " + k + '="' + v + '"'
            return prop_str
        return ""
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self,tag,value,props = None):
        super().__init__(tag=tag,value=value,props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("Leaf nodes must have a value")
        if self.tag == None:
            return self.value
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self,tag,children,props = None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        return_str = ""
        if not self.tag:
            raise ValueError("Parent nodes must have a tag")
        if self.children is None:
            raise ValueError("Parent nodes must have a children value")
        for child in self.children:
            return_str += child.to_html()
        return f"<{self.tag}>{return_str}</{self.tag}>"