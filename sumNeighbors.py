def search(arr, x):
    for i in range(0, len(arr)):
        if (arr[0]+arr[i]==x):
            return arr[i]
    return -1
arr = [-1, 2, 3, 7, 10]
x=1
arr1=[]
result=search(arr, x)
arr1.append(arr[0])
arr1.append(result)
print(arr1)
