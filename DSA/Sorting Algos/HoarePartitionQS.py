def selectionSort(list):
    for i in range(len(list)-1):
        for j in range(i+1,len(list)):
            if list[i]>list[j]:
                temp=list[i]
                list[i]=list[j]
                list[j]=temp
    return
def bubbleSort(list):
    n=len(list)
    for i in range(n-1):
        Swapped=False
        for j in range(n-1-i):
            if(list[j]>list[j+1]):
                temp=list[j+1]
                list[j+1]=list[j]
                list[j]=temp
                Swapped=True
        if not Swapped:
            print("O(n)")
            return


def swap(a,b,arr):
    arr[a],arr[b]=arr[b],arr[a]

def partition(start,end,arr):
    pivotIndex=start
    pivot=arr[start]
    while start<end:
        while arr[start]<=pivot:
            start+=1
        while arr[end]>pivot:
            end-=1
        if start<end:
            swap(start,end,arr)
    swap(end,pivotIndex,arr)
    return end

def quickSort(start,end,arr):
    if start<end:
        pi=partition(start,end,arr)
        quickSort(start,pi-1,arr)
        quickSort(pi+1,end,arr)

if __name__=="__main__":
    arr=[31,2,5,7,9,3,6,69,54,20]
    quickSort(0,len(arr)-1,arr)
    bubbleSort(arr)
    print(arr)