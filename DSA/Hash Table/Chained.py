class HashTable:
    def __init__(self):
        self.size=50
        self.arr=[[] for i in range(self.size)]
    def getHash(self,string):
        sum=0
        for char in string:
            sum+=ord(char)
        return sum % self.size
    def __setitem__(self,key,value):
        hashValue=self.getHash(key)
        found=False
        #Check if we are updating any key
        for i in range(len(self.arr[hashValue])):
            if self.arr[hashValue][i][0]==key:
                self.arr[hashValue][i]=(key,value)
                found=True
                break
        #Check if we are adding a new key
        if not found:
            self.arr[hashValue].append((key,value))
    def __getitem__(self,key):
        hashValue=self.getHash(key)
        for i in range(len(self.arr[hashValue])):
            if(self.arr[hashValue][i][0]==key):
                return self.arr[hashValue][i][1]
        return 0
    def __delitem__(self,key):
        hashValue=self.getHash(key)
        for i in range(len(self.arr[hashValue])):
            if(self.arr[hashValue][i][0]==key):
                self.arr[hashValue].pop(i)
                return
if __name__=="__main__":
    ht=HashTable()
    ht["march 6"]=69
    ht["march 6"]=90
    ht["march 17"]=96
    del(ht["march 17"])
    print(ht.arr)
    