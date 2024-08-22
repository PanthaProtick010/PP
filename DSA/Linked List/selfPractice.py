class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class linkedList:
    def __init__(self):
        self.head=None
    
    def insertInBeginning(self,data):
        node=Node(data,self.head)
        self.head=node
    
    def print(self):
        if self.head is None:
            print("The linked list is empty")
        else:
            empty=""
            itr=self.head
            while itr:
                empty+=(str(itr.data)+"-->")
                itr=itr.next
            empty+="Null"
            print(empty)
    def insertAtEnd(self,data):
        if(self.head is None):
            self.insertInBeginning(data)
        else:
            itr=self.head
            while itr.next:
                itr=itr.next
            itr.next=Node(data,None)
    def insertList(self,list):
        for items in list:
            self.insertAtEnd(items)
        return
    def getLen(self):
        itr=self.head
        count=0
        while itr:
            itr=itr.next
            count+=1
        return count
    def insertAt(self,index,data):
        if index==0:
            self.insertInBeginning(data)
        elif index<0 or index>self.getLen():
            print("Insertion not possible")
        else:
            itr=self.head
            count=0
            while itr:
                if(count==index-1):
                    itr.next=Node(data,itr.next)
                    return
                itr=itr.next
                count+=1
    def delete(self,index):
        if index==0:
            self.head=self.head.next
        elif index<0 or index>self.getLen():
            print("Insertion not possible") 
        else:
            itr=self.head
            count=0
            while itr:
                if count==index-1:
                    itr.next=itr.next.next
                    return
                itr=itr.next
                count+=1
    def insertAfterValue(self,dataAfter,data):
        itr=self.head
        while itr:
            if(itr.data==dataAfter):
                itr.next=Node(data,itr.next)
                return
            itr=itr.next
        print("The data wasn't found to insert after")
    def removeByValue(self,data):
        itr=self.head
        while itr.next:
            if itr.next.data==data:
                itr.next=itr.next.next
                return
            itr=itr.next
        print("The value wasn't found to delete")
if __name__=="__main__":
    ll=linkedList()
    ll.insertInBeginning(5)
    ll.insertInBeginning(15)
    ll.insertInBeginning(20)
    ll.print()

'''
def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node

def remove_by_value(self, data):
    # Remove first node that contains data
'''