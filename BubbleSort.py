
oldlist = [10, 75, 16, 65, 42, -5, 27, -7, 12, 88, 35, -22, 8, 48]

def bubble_sort(mylist):
    last_item = len(mylist) - 1
    for z in range (0, last_item):
        for x in range(0, last_item-z):
            if mylist[x] > mylist[x+1]:
                mylist[x], mylist[x+1] = mylist[x+1], mylist[x]

    return mylist

print("Old List: ", oldlist)
newlist = bubble_sort(oldlist).copy()
print("New List: ", newlist)
