def tree_insert(T, z):
    '''
    Insert node z to tree T
    '''
    y = None
    x = T.root
    while x != None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == None:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z

def transplant(T, u, v):
    '''
    Replace subtree with v
    '''
    if u.p == None:
        T.root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    if v != None:
        v.p = u.p


def tree_delete(T, z):
    '''
    Delete node z from tree T
    '''
    if z.left == None:
        transplant(T, z, z.right)
    elif z.right == None:
        transplant(T, z, z.left)
    else:
        y = tree_min(z.right)
        if y.p != z:
            transplant(T, y, y.right)
            y.right = z.right
            y.right.p = y
        transplant(T, z, y)
        y.left = z.left
        y.left.p = y
        
