class Queue():
    def __init__(self, n):
        # n is the # of elements the queue can hold
        self.n = n
        self.data = [None] * n
        self.head = 0 # the head of the queue
        self.tail = 0 # the index to the next available element
        self.free = n

    def empty(self):
        return self.free == self.n

    def full(self):
        return self.free == 0

    def enqueue(self, i):
        if self.full():
            raise Exception("Queue overflow!")
        self.data[self.tail] = i
        self.free -= 1
        self.tail = (self.tail + 1) % self.n

    def dequeue(self):
        if self.empty():
            raise Exception("No element in the queue")

        num = self.data[self.head]
        self.free += 1
        self.head = (self.head + 1) % self.n
        return num

    def __str__(self):
        res = ''
        i = 0
        while i < self.n - self.free:
            res += str(self.data[(self.head + i)%self.n])
            res += ', '
            i += 1
        return 'Queue data is: ' + res[:-2]

def test():
    queue = Queue(12)
    queue.head = 6
    queue.tail = 6
    queue.enqueue(15)
    queue.enqueue(6)
    queue.enqueue(9)
    queue.enqueue(8)
    queue.enqueue(4)
    print(queue.head, queue.tail, queue.free)
    print(queue)
    queue.enqueue(17)
    queue.enqueue(3)
    queue.enqueue(5)
    print(queue.head, queue.tail, queue.free)
    print(queue)
    queue.dequeue()
    print(queue.head, queue.tail, queue.free)
    print(queue)

def Ex10_1_3():
    queue = Queue(6)
    queue.enqueue(4)
    queue.enqueue(1)
    queue.enqueue(3)
    queue.dequeue()
    queue.enqueue(8)
    queue.dequeue()
    print(queue.head, queue.tail, queue.free)
    print(queue)

#test()
Ex10_1_3()
