def insert(left,right,arr):
    temp1=arr[right]
    for i in range(left,right+1):
            temp2=arr[i]
            arr[i]=temp1
            temp1=temp2

def calculateMedian(left,arr):
    if len(arr)==0: return 0
    size=left+1
    half=int(size/2)
    if size%2==0:
        ans=float(arr[half]+arr[half-1])/2
        ans=round(ans,2)
    else:
        ans=arr[half]
    return ans

def insertionSort(arr):
    left=0
    right=left+1
    end=len(arr)
    if end<2:
        print(str(calculateMedian(left,arr)))
        return
    while right!=end:
        #put left in correct position
        print(str(calculateMedian(left,arr)))
        while left>=0:
            if arr[left]>arr[right]:
                left-=1
            else:
                insert(left+1,right,arr)
                break
        if left==-1:
            insert(0,right,arr)
        right+=1
        left=right-1
    print(str(calculateMedian(left,arr)))

if __name__=="__main__":
    tests=[
        [11,9,29,7,2,15,28],
        [3,7,9,11],
        [25,22,21,10],
        [29,15,28],
        [],
        [6]
    ]
    for arr in tests:
        print(arr)
        insertionSort(arr)
        print(arr)
    