import math

class Heap():
    def __init__(self, A:list):
        self.data = A
        self.size = len(A)
        self.root = A[0]

    def left(self, i):
        '''
        Returns the index of left child of i
        '''
        idx = i * 2 + 1
        if idx >= self.size:
            return None
        return idx

    def right(self, i):
        '''
        Returns the index of right child of node i
        '''
        idx = i * 2 + 2
        return idx if idx < self.size else None

    def parent(self, i):
        '''
        Returns the parent of the given node
        Eg. data[6] -> data[2], data[5] -> data[2]
        '''
        if i == 0:
            # Root doesn't have a parent
            return None

        idx_parent = math.ceil(i/2) - 1
        return idx_parent
