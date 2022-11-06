def selectionSort(arr):
    newArr=[]
    for i in range(len(arr)):
        smallest = min(arr)
    newArr.append(smallest)
    return newArr
print (selectionSort([5,3,6,2,10]))