from textnode import *
import re

def main():
    print(block_to_block_type("1. \n2.\n3.\n4.\n5.\n6.\n7.\n8.\n9.\n10."))    

def block_to_block_type(block):
    if block[0] == "#":
        return "heading"
    if block[0] + block[1] + block[2] == "```" and block[-1] + block[-2] + block[-3] == "```":
        return "code"
    if all(line[0] == ">" for line in block.split("\n")):
        return "quote"
    if all(line[0] + line[1] == "* " or line[0] + line[1] == "- " for line in block.split("\n")):
        return "unordered_list"
    i=0
    for line in block.split("\n"):
        i += 1
        if not line.startswith(f"{i}."):
            return "paragraph"
    return "ordered_list"
        

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown syntax!")
        
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(sections[i], TextType.TEXT))
                continue
            else:
                new_nodes.append(TextNode(sections[i], text_type))

    return new_nodes    


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((https?:[a-zA-Z0-9./?_:=@&-]+)\)", text)
    

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((https?:[a-zA-Z0-9&?/_.=@:-]+)\)", text)


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes
            

def text_to_textnodes(text):
    text_node = TextNode(text, TextType.TEXT)
    node_list = [text_node]
    node_list = split_nodes_delimiter(node_list, "**", TextType.BOLD)
    node_list = split_nodes_delimiter(node_list, "*", TextType.ITALIC)
    node_list = split_nodes_delimiter(node_list, "`", TextType.CODE)
    node_list = split_nodes_image(node_list)
    node_list = split_nodes_link(node_list)

    return node_list


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for i in range(len(blocks)):
        blocks[i] = blocks[i].strip()
        if blocks[i] == "":
            continue
        filtered_blocks.append(blocks[i])

    return filtered_blocks




if __name__ == "__main__":
    main()

