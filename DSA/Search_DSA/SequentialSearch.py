def sequential_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

arr = [12, 45, 23, 67, 34, 89]
key = int(input())

result = sequential_search(arr, key)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")
