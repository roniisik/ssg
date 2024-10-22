from textnode import TextNode, TextType
def main():
    
    tn = TextNode("Hello", TextType.BOLD.value, "https://www.boot.dev")
    print(tn)
main()