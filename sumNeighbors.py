def search(arr, x):
    for i in range(0, len(arr)):
        if (arr[0]+arr[i]==x):
            return arr[i]
    return -1
arr = [-1, 2, 3, 7, 10]
x=9

result=search(arr, x)
print(result)
