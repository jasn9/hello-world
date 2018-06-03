print("Enter No.")
n = int(input())
arr = []
print("Enter Array")
for i in range(-1,n-1):
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
