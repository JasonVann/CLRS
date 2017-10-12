def os_rank(T, x):
    r = T.root.size + 1
    if x == T.root:
        return r
    elif x < T.root:
        return os_rank(T.left, x)
    else:
        return r + os_rank(T.right, x)
