def cocktailShakerSort(arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        right -= 1
        for i in range(right, left - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        left += 1
    return arr