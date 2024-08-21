from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()
        
    def enqueue(self, item):
        self.buffer.appendleft(item)

    def dequeue(self):
        self.buffer.pop()
        
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        print(len(self.buffer))
    
    
qu = Queue()
qu.enqueue(5)
qu.enqueue(15)
qu.enqueue(25)
qu.enqueue(35)
qu.size()
qu.buffer     
    
    