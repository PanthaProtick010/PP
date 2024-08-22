from collections import deque
class Stack:
    def __init__(self):
        self.container=deque()
    def push(self,value):
        self.container.push(value)
    def pop(self,value):
        self.container.pop(value)
    def peek(self):
        return self.container[-1]
    def isEmpty(self):
        return len(self.container)==0
    def size(self):
        return len(self.container)