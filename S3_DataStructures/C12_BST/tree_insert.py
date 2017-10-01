def tree_insert_recur(T, z):
    if T == None:
        T.root = z
        
    x = T.root
    if z.key < x.key:
        return tree_insert_recur(x.left, z)
    else:
        return tree_insert_recur(x.right, z)
