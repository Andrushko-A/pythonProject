def search(arr, x):
    for i in range(0, len(arr)):
        j=i+1
        for j in range(0, len(arr)):
            if (arr[i]+arr[j]==x):
                return arr[j]
    return -1
arr = [-1, 2, 3, 7, 10]
x=9
result=search(arr, x)
print(result)
