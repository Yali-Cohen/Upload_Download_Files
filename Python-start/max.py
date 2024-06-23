def max():
    numbers = [25,3,5,2,78,8,1,9,4]
    biggest = numbers[0]
    for item in range(1,len(numbers)-1):
        if biggest < numbers[item]:
            biggest = numbers[item]
    print(biggest)
    
max()
def even(arr):
    fun = lambda x:x
    result = [fun(item) for item in arr if item%2==0]
    return result

ls = even([1,4,5,7,8,10,13])
print(ls)
