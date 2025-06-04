from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        contents = node.text
        delimiters_found = 0
        while len(contents) > 0:
            if delimiter in contents:
                removed = contents[:contents.index(delimiter)+1]
            else:
                removed = contents
            delimiters_found += 1
            if delimiters_found % 2 != 0:
                new_nodes.append(TextNode(removed.replace(delimiter, ""), TextType.TEXT))
            else:
                new_nodes.append(TextNode(removed.replace(delimiter, ""), text_type))

            contents = contents.replace(removed, "")
    return new_nodes