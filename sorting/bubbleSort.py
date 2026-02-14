def bublle_sort(arr) :

    swapped = True

    while swapped :
        swapped = False
        for i in range(len(arr) - 1) :
            if(arr[i] > arr[i + 1]) :
                swap(arr , i , i + 1)
                swapped = True



def swap(arr , i , j) :
    arr[i] , arr[j] = arr[j] , arr[i]


arr = [5,4,3,2,1]
bublle_sort(arr)
print(arr)