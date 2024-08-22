class HashTable:
    def __init__(self):
        self.size=10
        self.arr=[None for i in range(self.size)]
    def getHash(self,key):
        sum=0
        for char in key:
            sum+=ord(char)
        return sum%self.size
    def __setitem__(self,key,value):
        h=self.getHash(key)
        if self.arr[h] is not None:
            if self.arr[h][0]==key:
                self.arr[h]=(key,value)
                return
            else:
                index=h+1
                while index!=h:
                    if index==self.size:
                        index=0
                    elif self.arr[index] is not None:
                        if self.arr[index][0]==key:
                            self.arr[index]=(key,value)
                            return
                        else:
                            index+=1
                    else:
                        self.arr[index]=(key,value)
                        return
                print("The list is full. Insertion failed of",key)
        else:
            self.arr[h]=(key,value)
            return
    def __getitem__(self,key):
        h=self.getHash(key)
        if self.arr[h]:
            if self.arr[h][0]==key:
                return self.arr[h][1]
            else:
                index=h+1
                while index!=h:
                    if index==self.size:
                        index=0
                        continue
                    if self.arr[index]:
                        if self.arr[index][0]==key:
                            return self.arr[index][1]
                        else:
                            index+=1
                    else:
                        return None
        else:
            return None
    def __delitem__(self,key):
        h=self.getHash(key)
        if self.arr[h]:
            if self.arr[h][0]==key:
                self.arr[h]=None
                return
            else:
                index=h+1
                while index!=h:
                    if index==self.size:
                        index=0
                        continue
                    if self.arr[index]:
                        if self.arr[index][0]==key:
                            self.arr[index]=None
                            return
                        else:
                            index+=1
                    else:
                        return
        else:
            return
if __name__=="__main__":
    ht=HashTable()
    ht["Jan 1"]=23
    ht["Jan 2"]=27
    ht["Jan 3"]=37
    ht["Jan 4"]=38
    ht["Jan 5"]=47
    ht["Jan 6"]=11
    ht["Jan 7"]=32
    ht["Jan 8"]=11
    ht["Jan 9"]=21
    ht["Jan 10"]=20
    ht["Jan 10"]=69
    print(ht.arr)