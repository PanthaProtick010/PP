class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class linkedList:
    def __init__(self):
        self.head=None
    def insertAtBeginning(self,data):
        node=Node(data, self.head)
        self.head=node
    def insertAtEnd(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        else:
            itr=self.head
            while itr.next:
                itr=itr.next
            itr.next=Node(data,None)
            return
    def printList(self):
        if self.head is None:
            print("Linked List is empty")
            return
        else:
            itr=self.head
            string=""
            while itr:
                string+=(str(itr.data)+"-->")
                itr=itr.next
            string+=("Null")
            print(string)
    def enterList(self,list):
        for item in list:
            self.insertAtEnd(item)
    def getLen(self):
        itr=self.head
        count=0
        while itr:
            count+=1
            itr=itr.next
        return count
    def delete(self,index):
        if(index>=self.getLen() or index<0):
            print("Index not found")
            return
        elif index==0:
           self.head=self.head.next
        else:
             itr=self.head
             count=0
             while itr:
                 if(count==index-1):
                     itr.next=itr.next.next
                     break
                 itr=itr.next
                 count+=1
    def insertAt(self,index,data):
        if(index>=self.getLen() or index<0):
            print("Index not found")
            return
        elif index==0:
           self.insertAtBeginning(data)
        else:
            itr=self.head
            count=0
            while itr:
                if count==index-1:
                    break
                itr=itr.next
                count+=1
            node=Node(data,itr.next)
            itr.next=node
            return       

if __name__=="__main__":
    linkedlist=linkedList()
    linkedlist.enterList([2,3,4,5,6,7])
    linkedlist.printList()
    print(str(linkedlist.getLen()))
    linkedlist.delete(2)
    linkedlist.printList()
    linkedlist.insertAt(2,69)
    linkedlist.printList()