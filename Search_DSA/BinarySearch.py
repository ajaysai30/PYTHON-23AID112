def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72]
target = 23

position = binary_search(numbers, target)

if position != -1:
    print("Found at index", position)
else:
    print("Not found")
