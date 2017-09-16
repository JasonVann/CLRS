# Ex12.2-3

def tree_pred(node):
    '''
    Returns the predecessor to a node in a BST
    '''
    if node.left:
        return tree_max(node.left)
    y = node.parent
    while y != None and node == y.left:
        node = y
        y = y.parent
    return y
