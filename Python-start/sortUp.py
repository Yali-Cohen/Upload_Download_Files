def sortedUp(ls):
    sortUp = True
    for item in range(1,len(ls)):
        if ls[item]<ls[item-1]:
            sortUp = False
            break
    if sortUp:
        print("The list is sorted up")
    else:
        print("The list isn't sorted up")
test_list = [1,2,3,4,5,2]
sortedUp(test_list)