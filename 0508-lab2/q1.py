def merge(list1, list2):
    i = j = 0
    merged = list()
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged


mylist1 = [44, 32, 31, 21, 11, 6, 5]
mylist2 = [34, 22, 17, 15, 13, 4, 2]
my_orderedlist = merge(mylist1, mylist2)
print(my_orderedlist)

mylist1 = ["Orange", "Lemon", "Apple"]
mylist2 = ["Watermelon", "Pear", "Melon", "Banana"]
my_orderedlist = merge(mylist1, mylist2)
print(my_orderedlist)
