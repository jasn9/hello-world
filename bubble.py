n = int(input())
arr = []
for i in range(0,n):
    n = int(input())
    arr.append(n)
n = len(arr)
for i in range(0,n):
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
           temp = arr[j]
           arr[j] = arr[j+1]
           arr[j+1] = temp
print(arr)    
