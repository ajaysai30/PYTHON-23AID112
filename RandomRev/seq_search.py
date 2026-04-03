def seq_search(arr,item):
    idx=0
    while idx<len(arr):
        if arr[idx]==item:
            return idx
        idx+=1
    return None
arr=[2,6,5,4,3,9,8]
print(seq_search(arr,9))
