def quickSort(arr, lowIndex, highIndex):

    if lowIndex >= highIndex:
        return

    pivot = arr[highIndex]
    lp = lowIndex
    rp = highIndex - 1

    while lp <= rp:
        while lp <= rp and arr[lp] <= pivot:
            lp += 1

        while lp <= rp and arr[rp] >= pivot:
            rp -= 1

        if lp < rp:
            swap(arr, lp, rp)

    swap(arr, highIndex, lp)

    quickSort(arr, lowIndex, lp - 1)
    quickSort(arr, lp + 1, highIndex)


def swap(arr, firstidx, secondidx):
    arr[firstidx], arr[secondidx] = arr[secondidx], arr[firstidx]


arr = [5,4,3,2,1]
quickSort(arr, 0, len(arr) - 1)
print(arr)
