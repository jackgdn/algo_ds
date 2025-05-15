def pivot(mylist, l, r):
    return r


def partition(mylist, l, r, pivot_index):
    pivot_value = mylist[pivot_index]
    mylist[pivot_index], mylist[r] = mylist[r], mylist[pivot_index]
    temp_index = l
    for i in range(l, r):
        if mylist[i] < pivot_value:
            mylist[i], mylist[temp_index] = mylist[temp_index], mylist[i]
            temp_index += 1
    mylist[temp_index], mylist[r] = mylist[r], mylist[temp_index]
    return temp_index


def quicksort(mylist, l, r):
    if l < r:
        pi = pivot(mylist, l, r)
        k = partition(mylist, l, r, pi)
        print("pivot=" + str(mylist[k]) + " " + "L=" + str(l) + " " + "R=" + str(r))
        print(mylist)
        quicksort(mylist, l, k - 1)
        quicksort(mylist, k + 1, r)


mylist = [23, 12, 31, 21, 41, 3, 1]
print(mylist)
quicksort(mylist, 0, len(mylist) - 1)
print(mylist)

mylist = [44, 32, 31, 21, 11, 6, 5]
print(mylist)
quicksort(mylist, 0, len(mylist) - 1)
print(mylist)
