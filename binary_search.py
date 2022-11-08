def binary_search(list, item):
    low=-1
    high=len(list)

    while high-low>1:
        mid=int((low+high)/2)
        guess=list[mid]
        if guess==item:
            return mid
        if guess>item:
            high=mid-1
        else:
            low=mid+1
    return None

my_list = [1,3,5,7,9]
print(binary_search(my_list, 9))



