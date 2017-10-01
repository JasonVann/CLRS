# Ex13.2.1

def right_rotate(T, y):
    '''
    Perform right-rotate on Tree's node y
    '''
    x = y.left
    y.left = x.right
    x.p = y.p
    if x.right != T.nil:
        x.right.p = y
    if x.p == T.nil:
        T.root = x
    elif y.p.left == y:
        y.p.left = x
    else:
        y.p.right = x
    x.right = y
    y.p = x
