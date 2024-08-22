from collections import deque
class Queue:
    def __init__(self):
        self.q=deque()
    def push(self,value):
        self.q.appendleft(value)
    def pop(self):
        self.q.pop()
    def peek(self):
        return self.q[-1]
    def size(self):
        return len(self.q)
    def isEmpty(self):
        return self.size()==0