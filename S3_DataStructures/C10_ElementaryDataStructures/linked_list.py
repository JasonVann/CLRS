class Node():
    def __init__(self, val):
        self.prev = None
        self.next = None
        self.val = val

    def __str__(self):
        res = ''
        #if self.prev:
        #    res += str(self.prev) + ', '
        res += str(self.val)
        return res

class Linked_List():
    def __init__(self, head = None):
        if head:
            self.head = Node(head)
        else:
            self.head = None

    @property
    def next(self):
        if self.head == None or self.head.next == None:
            return None
        return Linked_List(self.head.next)

    def search(self, v):
        # Search for node with val = v
        # Returns None if not found
        x = self.head
        while x and x.val != v:
            x = x.next
        return x

    def insert(self, x):
        # Insert value x to the front of the list
        head = self.head
        new_head = Node(x)
        new_head.next = head
        if head:
            head.prev = new_head
        self.head = new_head

    def delete(self, v):
        # Delete value v from the list
        node = self.search(v)
        if node:
            prev = node.prev
            next_node = node.next
            if prev:
                prev.next = next_node
            else:
                # v is the head
                self.head = next_node
            if next_node:
                next_node.prev = prev

def test():
    ll = Linked_List(1)
    ll.insert(4)
    ll.insert(16)
    ll.insert(9)
    res = ll.search(1)
    print(res)
    ll.delete(4)
    res = ll.search(1)
    print(res)
    print(ll.head)

#test()
