class BinarySearchTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if data==self.data:
            return 
        elif data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements+=self.right.in_order_traversal()
        return elements
    
    def search(self,value):
        if self.data==value:
            return True
        elif value<self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        else:
            if self.right:
                return self.right.search(value)
            else:
                return False
    
    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data
        
    def find_max(self):
        if self.right:
            return self.right.find_min()
        else:
            return self.data
        
    def calculate_sum(self):
        sum=0
        if self.left:
            sum+=self.left.in_order_traversal()
        sum+=self.data
        if self.right:
            sum+=self.right.in_order_traversal()
        return sum
    
    def pre_order_traversal(self):
        elements=[]
        elements.append(self.data)
        if self.left:
            elements+=self.left.pre_order_traversal()
        if self.right:
            elements+=self.right.pre_order_traversal()
        return elements
    
    def post_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.post_order_traversal()
        if self.right:
            elements+=self.right.post_order_traversal()
        elements.append(self.data)
        return elements
    
    def delete(self,value):
        if value<self.data:
            if self.left:
                self.left.delete(value)
        elif value>self.data:
            if self.right:
                self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            
            max=self.left.find_max()
            self.data=max
            self.left=self.left.delete(max)
            return self
    
def build_tree(elements):
    root=BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root
if __name__=="__main__":
    arr=[17,4,1,20,9,23,18,34]
    tree=build_tree(arr)