class Node:
    def __init__(self,data=None,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next
class doubleLinkedList:
    def __init__(self):
        self.head=None
    def insertInBeginning(self,data):
        if self.head:
            node=Node(data,None,self.head)
            self.head=node
        else:
            self.head=Node(data,None,None)
    def insertAtEnd(self,data):
        if self.head:
            itr=self.head
            while itr.next:
                itr=itr.next
            itr.next=Node(data,itr,None)
        else:
            self.insertInBeginning(data)
    def getLen(self):
        itr=self.head
        count=0
        while itr:
            itr=itr.next
            count+=1
        return count
    def insertAt(self,index,data):
        len=self.getLen()
        if index<0 or index>len:
            print("Insertion not possible")
        elif index==0:
            self.insertInBeginning(data)
        elif index==len:
            self.insertAtEnd(data)
        else:
            itr=self.head
            count=0
            while itr:
                if count==index-1:
                    node=Node(data,itr,itr.next)
                    itr.next=node
                    node.next.prev=node
                    return
                itr=itr.next
                count+=1
    def insertList(self,list):
        for item in list:
            self.insertAtEnd(item)
        return
    def deleteAt(self,index):
        len=self.getLen()
        if index==0:
            self.head=self.head.next
            self.prev=None
        elif index<0 or index>=len:
            print("Deletion not possible")
        else:
            itr=self.head
            count=0
            while itr:
                if count==index-1:
                    itr.next=itr.next.next
                    itr.next.prev=itr
                    return
                itr=itr.next
                count+=1
    def printForward(self):
        if self.head:
            itr=self.head
            empty=""
            while itr:
                empty+=(str(itr.data)+"-->")
                itr=itr.next
            empty+="Null"
            print(empty)
        else:
            print("The Linked List is empty")
    def printBackward(self):
        if self.head:
            itr=self.head
            while itr.next:
                itr=itr.next
            empty="Null<--"
            while itr:
                empty+=(str(itr.data)+"<--")
                itr=itr.prev
            empty+="Null"
            print(empty)
            return
        else:
            print("The List is empty")
if __name__=="__main__":
    dll=doubleLinkedList()
    dll.insertInBeginning(2)
    dll.insertAtEnd(3)
    dll.printForward()
    dll.insertList([3,4,5,6,7])
    dll.printBackward()
    dll.deleteAt(2)
    dll.printForward()
    dll.insertAt(2,69)
    dll.printForward()