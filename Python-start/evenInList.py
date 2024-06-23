def even(arr):#first way
    fun = lambda x:x
    result = [fun(item) for item in arr if item%2==0]
    return result

def evenSecond(arr):#second way
    evenList=[]
    for item in arr:
        if item%2==0:
            evenList.append(item)
    return evenList

ls = even([1,4,5,7,8,10,13])
print(ls)
ls2 = evenSecond([1,4,5,7,8,10,13])
print(ls)