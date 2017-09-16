def tree_min(node):
    if node.left:
        return tree_min(node.left)
    return node

def tree_max(node):
    if node.right:
        return tree_min(node.right)
    return node
