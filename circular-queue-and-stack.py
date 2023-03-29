# Implemented using fake arrays
# Circular queue. Can be a linear queue if the code that rolls over pointers is deleted.
class CircularQueue:
    def __init__(self, length):
        self.capacity = length
        self.size = 0
        self.queue = [None] * length
        self.head = 0
        self.nextFree = 0

    def isFull(self):
        # alternatively could use nextFree - head - 1 for size
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, item):
        # Check if full
        if self.isFull():
            return
    
        self.queue[self.nextFree] = item
        self.nextFree = self.nextFree + 1
        self.size = self.size + 1

        # This part makes it circular
        if self.nextFree > self.capacity:
            self.nextFree = 0

    def dequeue(self):
        # Check if empty
        if self.isEmpty():
          return
    
        item = self.queue[self.head]
    
        self.head = self.head + 1
        self.size = self.size - 1

        # This part makes it ciruclar
        if self.head > self.capacity:
            self.head = 0

        return item

# Stack
class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stackArray = [None] * capacity
        self.top = 0

    def isEmpty(self):
        if self.top <= 0:
            return True
        return False

    def isFull(self):
        if self.top >= self.capacity:
            return True

    def push(self, item):
        # Check if full before pushing
        if self.isFull():
            print("Stack full")
            return False

        # Push
        self.stackArray[self.top] = item
        self.top = self.top + 1

    def pop(self):
        # Check if empty before poppingß
        if self.isEmpty():
            print("Stack empty")
            return None

        # Pop
        self.top = self.top - 1
        return self.stackArray[self.top]

    def peek(self):
        return self.stackArray[self.top - 1]
    
# Test the stack
print("Testing stack: \n")
testStack = Stack(5)
testStack.push("1")
testStack.push("2")
testStack.push("3")
print(testStack.pop())
testStack.push("3 replacement")
testStack.push("4")
testStack.push("5")
testStack.push("6")

print(testStack.peek())

# Iterate from 0 to 6
for i in range(7):
    print(testStack.pop())

print("Testing queue: \n")

# Test the queue
testQueue = CircularQueue(4)
testQueue.enqueue("1")
testQueue.enqueue("2")
testQueue.enqueue("3")
testQueue.enqueue("4")
testQueue.enqueue("5")
print(testQueue.dequeue())
print(testQueue.dequeue())
print(testQueue.dequeue())
print(testQueue.dequeue())
print(testQueue.dequeue())