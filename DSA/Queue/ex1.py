from collections import deque
import time
import threading
class Queue:
    def __init__(self):
        self.q=deque()
    def push(self,value):
        self.q.appendleft(value)
    def pop(self):
        return self.q.pop()
    def peek(self):
        return self.q[-1]
    def size(self):
        return len(self.q)
    def isEmpty(self):
        return self.size()==0
    def copy(self):
        temp=Queue()
        temp.q=deque(self.q)
        return temp

def takeOrders(list,queue):
    for items in list:
        queue.push(items)
        time.sleep(0.5)

def serveOrders(queue):
    while not queue.isEmpty():
        print(f"{queue.pop()} has been successfully served")
        time.sleep(2)

if __name__=="__main__":
    q=Queue()
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1=threading.Thread(target=takeOrders,args=(orders,q))
    t2=threading.Thread(target=serveOrders,args=(q,))
    t1.start()
    time.sleep(1)
    t2.start()
    t1.join()
    t2.join()
    print(f"{time.time()} elapsed")    