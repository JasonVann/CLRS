from linked_list import Node, Linked_List

def reverse(head: Node):
    '''A recursive method that reverses nodes in a singly linked list
    '''
    x = head
    res = x
    if x.next:
        res = reverse(x.next)
        res.next = x
    return res

def reverse_loop(head):
    '''
    A non-recursive method that reverses nodes in a singly linked list
    '''
    prev = head
    cur = head.next
    prev.next = None
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    return prev

def test():
    ll = Linked_List(1)
    ll.insert(4)
    ll.insert(16)
    ll.insert(9)
    print(ll.head)
    res = reverse_loop(ll.head)
    print(res)
    print(res.next)
    print(res.next.next)
    print(res.next.next.next)

test()
