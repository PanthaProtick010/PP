def swap(a,b,arr):
    arr[a],arr[b]=arr[b],arr[a]

def partition(start,end,arr):
    i=start
    j=i
    pivot=arr[end]
    while j<=i:
        while arr[i]<pivot:
            i+=1
        if i==end:
            return end
        else:
            j=i+1
            while arr[j]>pivot:
                j+=1
            swap(i,j,arr)
            if j==end:
                return i
            else:
                i+=1
                j=i

def quickSort(start,end,arr):
    if start<end:
        pi=partition(start,end,arr)
        quickSort(start,pi-1,arr)
        quickSort(pi+1,end,arr)



if __name__=="__main__":
    arr=[31,2,5,20,7,9,3,6,69,54,20]
    quickSort(0,len(arr)-1,arr)
    print(arr)