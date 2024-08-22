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
    def append(self,key,num):
        h=self.getHash(key)
        for i in range(len(self.arr[h])):
            if self.arr[h][i][0]==key:
                value=self.arr[h][i][1]+num
                self.arr[h][i]=(key,value)
                return
        self.arr[h].append((key,num))
        return
if __name__=="__main__":
    ht=HashTable()
    with open("D:\\Python\\DSA\\Hash Table\\poems.txt", "r") as f:
        for line in f:
            tokens=line.split(" ")
            for item in tokens:
                item=item.lower()
                empty=""
                entered=False
                for letter in item:
                    if 'a'<=letter<='z' or 'A'<=letter<='Z':
                        empty+=letter
                    else:
                        if empty:
                            ht.append(empty, 1)
                        entered = True
                        break
                if not entered and empty:
                    ht.append(empty,1)
    print(str(ht["i"]))