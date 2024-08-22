arr=[]
n=int(input("Enter array size: "))
for i in range(n):
    arr.append(int(input("Enter index "+str(i)+": ")))
x=int(input("Enter the number you want to delete: "))
if x in arr:
    occurance=0
    for d in arr:
        if d==x:
            occurance+=1
    for d in range(occurance):
        arr.remove(x)
    print("The updated array: ")
    print(arr)
else:
    print("The value doesn't exist")