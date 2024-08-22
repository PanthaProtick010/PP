class HashTable:
    def __init__(self):
        self.size=100
        self.arr=[[] for i in range(self.size)]
    def getHash(self,key):
        sum=0
        for char in key:
            sum+=ord(char)
        return sum%self.size
    def __setitem__(self,key,value):
        h=self.getHash(key)
        for i in range(len(self.arr[h])):
            if self.arr[h][i][0]==key:
                self.arr[h][i]=(key,value)
                return
        self.arr[h].append((key,value))
        return
    def __getitem__(self,key):
        h=self.getHash(key)
        for i in range(len(self.arr[h])):
            if self.arr[h][i][0]==key:
                return self.arr[h][i][1]
        return None
    def __delitem__(self,key):
        h=self.getHash(key)
        for i in range(len(self.arr[h])):
            if self.arr[h][i][0]==key:
                self.arr[h].pop(i)
                return
        return
if __name__=="__main__":
    with open("D:\\Python\\DSA\\Hash Table\\ex1&2.csv", "r") as f:
        ht=HashTable()
        next(f)
        for line in f:
            tokens=line.split(',')
            ht[tokens[0]]=int(tokens[1])
    print(f"The temp on Jan 9 is {ht['Jan 9']}")
    print(f"The temp on Jan 4 is {ht['Jan 4']}")