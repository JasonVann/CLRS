def preorder(node):
    if node:
        print(node.key)
        if node.left:
            preorder(node.left)
        if node.right:
            preorder(node.right)

def postorder(node):
    if node:
        if node.left:
            preorder(node.left)
        if node.right:
            preorder(node.right)

        print(node.key)
