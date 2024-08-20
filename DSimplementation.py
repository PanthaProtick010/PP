class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def insertAtBeginning(self,value):
        self.head=Node(value,self.head)
    def insertInEnd(self,value):
        if self.head:
            itr=self.head
            while itr.next:
                itr=itr.next
            itr.next=Node(value,None)
        else:
            self.head=Node(value,None)
    def size(self):
        if self.head:
            itr=self.head
            count=1
            while itr.next:
                itr=itr.next
                count+=1
            return count
        else:
            return 0
    def insertAt(self,index,value):
        if(index<0 or index>self.size()):
            print("Insertion not possible")
        elif(index==0):
            self.insertAtBeginning(value)
        else:
            count=0
            itr=self.head
            while itr:
                if count==index-1:
                    itr.next=Node(value,itr.next)
                    return
                itr=itr.next
                count+=1
    def insertList(self,list):
        for item in list:
            self.insertInEnd(item)
    def print(self):
        if self.head:
            itr=self.head
            while itr:
                print(f"{itr.data}-->")
                itr=itr.next
            print("None")
        else:
            print("List is Empty")
    def deleteAt(self,index):
        if(index<0 or index>=self.size()):
            print("Deletion not possible")
        elif(index==0):
            self.head=self.head.next
        else:
            count=0
            itr=self.head
            while itr:
                if count==index-1:
                    itr.next=itr.next.next
                    return
                itr=itr.next
                count+=1
    def insertAfterValue(self,value,entry):
        itr=self.head
        while itr:
            if(itr.data==value):
                itr.next=Node(entry,itr.next)
                return
            itr=itr.next
        print("Value not found")
    def deleteValue(self,value):
        if self.head.data==value:
            self.head=self.head.next
            return
        itr=self.head
        while itr.next:
            if(itr.next.data==value):
                itr.next=itr.next.next
                return
            itr=itr.next
        print("Value not found")



class Tree:
    def __init__(self,data):
        self.data=data
        self.child=[]
        self.parent=None

    def addChild(self,node):
        node.parent=self
        self.child.append(node)

    def getLevel(self):
        level=0
        itr=self
        while itr.parent:
            itr=itr.parent
            level+=1
        return level
    
    def printTree(self):
        space=" "*self.getLevel()*4
        if self.getLevel()!=0:
            space+="|__"
        print(f"{space}{self.name}")
        for ch in self.child:
            ch.printTree()


class BST:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def addChild(self,data):
        if data==self.data:
            return
        elif data<self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left=BST(data)
        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right=BST(data)

    def inOrderTraversal(self):
        arr=[]
        if self.left:
            arr+=self.left.inOrderTraversal()
        arr+=[self.data]
        if self.right:
            arr+=self.right.inOrderTraversal()
        return arr
    
    def postOrderTraversal(self):
        arr=[]
        if self.left:
            arr+=self.left.inOrderTraversal()
        if self.right:
            arr+=self.right.inOrderTraversal()
        arr+=[self.data]
        return arr
    
    def preOrderTraversal(self):
        arr=[]
        arr+=[self.data]
        if self.left:
            arr+=self.left.inOrderTraversal()
        if self.right:
            arr+=self.right.inOrderTraversal()
        return arr
    
    def search(self,data):
        if self.data==data:
            return True
        elif data<self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        else:
            if self.right:
                return self.right.search(data)
            else:
                return False
            
    def findMin(self):
        if self.left:
            return self.left.findMin()
        else:
            return self.data
        
    def findMax(self):
        if self.right:
            return self.right.findMax()
        else:
            return self.data
        
    def delete(self,value):
        if value<self.data:
            if self.left:
                self.left=self.left.delete(value)
            
        elif value>self.data:
            if self.right:
                self.right=self.right.delete(value)
            
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                min=self.right.findMin()
                self.data=min
                self.right=self.right.delete(min)
                return self

def build_tree(elements):
    root=BST(elements[0])
    for i in range(1,len(elements)):
        root.addChild(elements[i])
    return root

class Graph:
    def __init__(self,edges):
        self.dic={}
        for start,end in edges:
            if start in self.dic:
                self.dic[start].append(end)
            else:
                self.dic[start]=[end]

    def getPath(self,start,end,history=[]):
        history=history+[start]
        if start==end:
            return [history]
        if start not in self.dic:
            return []
        else:
            pathChoices=[]
            for stops in self.dic[start]:
                if stops not in history:
                    paths=self.getPath(stops,end,history)
                    for items in paths:
                        pathChoices.append(items)
            return pathChoices
        
    def shortestPath(self,start,end,history=[]):
        history=history+[start]
        if start==end:
            return history
        if start not in self.dic:
            return None
        else:
            ans=None
            for stops in self.dic[start]:
                if stops not in history:
                    path=self.shortestPath(stops,end,history)
                    if path:
                        if ans is None or len(ans)>len(path):
                            ans=path
            return ans

def swap(a,b,arr):
    arr[a],arr[b]=arr[b],arr[a]

def hoarePartition(start,end,arr):
    lp=start
    rp=end
    pivot=arr[start]
    while lp<rp:
        while lp<=end and arr[lp]<=pivot:
            lp+=1
        if lp==end:
            if arr[lp]>pivot:
                swap(lp-1,start,arr)
                return lp-1
            else:
                swap(lp,start,arr)
                return lp
        else:
            while rp>=start and arr[rp]>pivot:
                rp-=1
            if rp>lp:
                swap(lp,rp,arr)
    swap(rp,start,arr)
    return rp
            
def lomutoPartition(start,end,arr):
    pivot=arr[end]
    i=start
    j=-1

    while j<i:
        while i<end and arr[i]<pivot:
            i+=1
        if i==end: return end
        else:
            j=i+1
            while arr[j]>pivot:
                j+=1
            swap(i,j,arr)
            if j==end:
                return i
            else:
                i+=1
                j=-1

    
def quickSort(start,end,arr):
    if start<end:
        pi=lomutoPartition(start,end,arr)
        quickSort(start,pi-1,arr)
        quickSort(pi+1,end,arr)

def mergeArr(a,b,arr,key,des):
    lenA=len(a)
    lenB=len(b)
    i=j=k=0
    while i<lenA and j<lenB:
        if des:
            if a[i][key]>b[j][key]:
                arr[k]=a[i]
                i+=1
            else:
                arr[k]=b[j]
                j+=1
        else:
            if a[i][key]<b[j][key]:
                arr[k]=a[i]
                i+=1
            else:
                arr[k]=b[j]
                j+=1
        k+=1
    while i<lenA:
        arr[k]=a[i]
        i+=1
        k+=1
    while j<lenB:
        arr[k]=b[j]
        j+=1
        k+=1
    return

def mergeSort(arr,key,des=False):
    size=len(arr)
    if size<=1:
        return
    else:
        mid=size//2
        arr1=arr[:mid]
        arr2=arr[mid:]
        mergeSort(arr1,key,des)
        mergeSort(arr2,key,des)
        mergeArr(arr1,arr2,arr,key,des)
        return
    
def shellSort(arr):
    size=len(arr)
    gap=size//2

    while gap>0:
        for i in range(gap,size):
            anchor=arr[i]
            j=i
            while j>=gap and arr[j-gap]>anchor:
                arr[j]=arr[j-gap]
                j-=gap
            arr[j]=anchor
        gap=gap//2
    
if __name__=="__main__":
    arr=[]
    shellSort(arr)
    print(arr)