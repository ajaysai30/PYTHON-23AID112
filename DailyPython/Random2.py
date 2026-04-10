n = int(input())
arr = list(map(int, input().split()))
k = int(input())

count = 0
left = 0
current_sum = 0

for right in range(n):
    current_sum += arr[right]
    
    while current_sum > k and left <= right:
        current_sum -= arr[left]
        left += 1
    
    if current_sum == k:
        count += 1

print(count)
