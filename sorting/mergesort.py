def mergeSort(arr) :
    if len(arr) < 2 :
        return

    leftarr = []
    rightarr = []

    for i in range(len(arr) // 2) :
        leftarr.append(arr[i])

    for i in range(len(leftarr) , len(arr)) :
        rightarr.append(arr[i])

    mergeSort(leftarr)
    mergeSort(rightarr)

    merge(arr , leftarr , rightarr)



def merge(arr , leftarr , rightarr) :
    ln = 0
    rn = 0
    k =  0

    while ln < len(leftarr) and rn < len(rightarr) :
        if leftarr[ln] < rightarr[rn] :
            arr[k] = leftarr[ln]
            k += 1
            ln += 1
        else :
            arr[k] = rightarr[rn]
            k += 1
            rn += 1


    while ln < len(leftarr) :
        arr[k] = leftarr[ln]
        ln += 1
        k += 1

    while rn < len(rightarr) :
        arr[k] = rightarr[rn]
        rn += 1
        k += 1


arr = [5,4,3,2,1]
mergeSort(arr)
print(arr)
