def inorder(node):
    stack = []
    while len(stack) != 0 or node != None:
        if node != None:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            print(node.key)
            node = node.right
            
