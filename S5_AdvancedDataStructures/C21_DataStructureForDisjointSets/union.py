class Node():
    def __init__(self, i):
        self.i = i
        self.p = self.i
        self.rank = 0

def union(x, y):
    link(find_set(x), find_set(y))

def link(x, y):
    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y
        if x.rank == y.rank:
            y.rank += 1

def find_set(x):
    if x.i != x.p:
        x.p = find_set(x.p)
    return x.p
