class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def insertAtBeginning(self,value):
        node=Node(value)
        Node.next=self.head
        self.head=Node
    def insertInEnd(self,value):
        if self.head:
            itr=self.head
            while itr.next:
                itr=itr.next
            itr.next=Node(value)
        else:
            self.insertAtBeginning(value)
    def getSize(self):
        if self.head:
            count=0
            itr=self.head
            while itr:
                itr=itr.next
                count+=1
            return count
        else:
            return 0
    def insertArr(self,arr):
        for items in arr:
            if self.head:
                self.insertInEnd(items)
            else:
                self.insertAtBeginning(items)
    def deleteByValue(self,value):
        if self.head.data==value:
            self.head=self.head.next
        else:
            itr=self.head
            while itr.next:
                if itr.next.data==value:
                    itr.next=itr.next.next
                    return
                itr=itr.next

    def deleteAt(self,index):
        if index<0 or index>=self.getSize():
            return
        elif index==0:
            self.head=self.head.next
        else:
            count=0
            itr=self.head
            while itr.next:
                if count==index-1:
                    itr.next=itr.next.next
                    return
                itr=itr.next
                count+=1