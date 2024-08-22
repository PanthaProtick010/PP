x=int(input("Enter the max number: "))
arr=[]
for i in range(1,x+1):
    if(i%2==1):
        arr.append(i)
print(arr)