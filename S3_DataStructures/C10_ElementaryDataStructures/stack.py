class Stack():
    def __init__(self, n):
        self.data = [None] * n
        self.capacity = n
        #self.size = 0
        self.top = -1 # refers to the last occupied index

    def push(self, num):
        if self.top == self.capacity:
            raise Exception('Stack overflow!')

        self.top += 1
        self.data[self.top] = num

    def pop(self):
        if self.empty():
            raise Exception('Stack underflow!')

        res = self.data[self.top]
        self.top -= 1

        return res

    def empty(self):
        return self.top == -1

    def __str__(self):
        res = ''
        for i in range(self.top+1):
            res += str(self.data[i])
            res += ', '

        return 'Stack data is: ' + res[:-2]

def test():
    stack = Stack(7)
    # stack.pop()
    stack.push(15)
    stack.push(6)
    stack.push(2)
    stack.push(9)
    print(stack)
    print(stack.top)
    stack.push(17)
    stack.push(3)
    print(stack)
    print(stack.top)
    res = stack.pop()
    print(res)
    print(stack)
    print(stack.top)

test()
