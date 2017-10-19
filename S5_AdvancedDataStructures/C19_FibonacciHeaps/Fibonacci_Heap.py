class Fib_Heap():
    def __init__(self):
        H.n = 0
        H.min = None
        H.root_list = []

class Fib_Node():
    def __init__(self, key):
        x.degree = 0
        x.p = None
        x.child = None
        x.left = None
        x.right = None
        x.mark = False
        x.key = key

def make_fib_heap():
    return Fib_Heap()

def fib_heap_insert(H, x):
    x.degree = 0
    x.p = None
    x.child = None
    x.mark = False
    if H.min == None:
        H.root_list.append(x)
        H.min = x
    else:
        H.root_list.append(x)
        if x.key < H.min.key:
            H.min = x
    H.n += 1

def fib_heap_union(H1, H2):
    H = make_fib_heap()
    H.min = H1.min
    H.root_list = H1.root_list
    H.root_list += H2.root_list
    if H1.min == None or (H2.min != None and H2.min.key < H1.min.key):
        H.min = H2.min
    H.n = H1.n + H2.n
    return H

def fib_heap_extract_min(H):
    z = H.min
    if z != None:
        for child in z.child:
            H.root_list.append(child)
            child.p = None
        H.root_list.remove(z)
        if z == z.right:
            H.min = None
        else:
            H.min = z.right
            consolidate(H)
        H.n -= 1
    return z

def consolidate(H):
    # reduce the # of trees
    A = [None] * D(H.n)
    for w in H.root_list:
        x = w
        d = x.degree
        while d > len(A):
            A.append(None)
        while A[d] != None:
            y = A[d]
            if x.key > y.key:
                x, y = y, x
            fib_heap_link(H, y, x)
            A[d] = None
            d += 1
        A[d] = x
    H.min = None
    for i in range(0, D(H.n)+1):
        if A[i] != None:
            if H.min == None:
                H.root_list = [A[i]]
                H.min = A[i]
            else:
                H.root_list.append(A[i])
                if A[i].key < H.min.key:
                    H.min = A[i]

def D(n):
    import math
    thi = 0.5*(math.sqrt(5)+1)
    return math.ceil(math.log(n, thi))

def fib_heap_link(H, y, x):
    H.root_list.remove(y)
    x.child.append(y)
    x.degree += 1
    y.makr = False

def fib_heap_decrease_key(H, x, k):
    if k > x.key:
        raise "New key is greater than current key"
    x.key = k
    y = x.p
    if y != None and x.key < y.key:
        cut(H, x, y)
        cascading_cut(H, y)
    if x.key < H.min.key:
        H.min = x

def cut(H, x, y):
    y.child.remove(x)
    y.degree -= 1
    H.root_list.append(x)
    x.p = None
    x.mark = False

def cascading_cut(H, y):
    z = y.p
    if z != None:
        if y.mark == False:
            y.mark = True
        else:
            cut(H, y, z)
            cascading_cut(H, z)

def fib_heap_delete(H, x):
    fib_heap_decrease_key(H, x, float('-inf'))
    fib_heap_extract_min(H)
