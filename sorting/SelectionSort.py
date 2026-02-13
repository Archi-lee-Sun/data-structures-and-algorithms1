def selectionSort(arr) :

    for i in range(len(arr) - 1) :
        min_idx = findMinIndex(arr , i)
        swap(arr , min_idx , i)



def findMinIndex(arr , start) :

     min_idx = start

     for i in range(start + 1 , len(arr)) :
         if arr[i] < arr[min_idx] :
             min_idx = i

     return min_idx

def swap(arr, firstidx, secondidx):
    arr[firstidx], arr[secondidx] = arr[secondidx], arr[firstidx]



arr = [5,4,3,2,1]
selectionSort(arr)
print(arr)