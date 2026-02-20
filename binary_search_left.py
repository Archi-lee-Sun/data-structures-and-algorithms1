def binary_search_left(arr,target) :
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right :
        mid = (left + right) // 2

        if arr[mid] == target :
            result = mid
            right = mid - 1

        elif arr[mid] > target :
            right = mid - 1

        else :
            left = mid + 1

            
    return result