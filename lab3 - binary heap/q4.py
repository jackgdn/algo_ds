class Node:
    def __init__(self, init_data):
        self.data = init_data

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data


class minBHeap:
    def __init__(self):
        self.a = []

    def is_empty(self):
        return len(self.a) == 0

    def Insert(self, item):
        node = Node(item)
        self.a.append(node)

        current_idnex = len(self.a) - 1
        parent_index = (current_idnex - 1) // 2

        while self.a[current_idnex].get_data() < self.a[parent_index].get_data():
            self.a[current_idnex], self.a[parent_index] = (
                self.a[parent_index],
                self.a[current_idnex],
            )
            current_idnex = parent_index
            parent_index = (current_idnex - 1) // 2
            if parent_index < 0:
                break

    def FindMin(self):
        return self.a[0].get_data()

    def Delete(self):
        self.a[0] = self.a[-1]
        self.a.pop()

        current_index = 0
        left_child_index = 2 * current_index + 1
        right_child_index = 2 * current_index + 2

        while left_child_index < len(self.a):
            if (
                right_child_index < len(self.a)
                and self.a[current_index].get_data()
                > self.a[right_child_index].get_data()
                < self.a[left_child_index].get_data()
            ):
                self.a[current_index], self.a[right_child_index] = (
                    self.a[right_child_index],
                    self.a[current_index],
                )
                current_index = right_child_index
            elif self.a[current_index].get_data() > self.a[left_child_index].get_data():
                self.a[current_index], self.a[left_child_index] = (
                    self.a[left_child_index],
                    self.a[current_index],
                )
                current_index = left_child_index
            else:
                break
            left_child_index = 2 * current_index + 1
            right_child_index = 2 * current_index + 2

    def Sort(self):
        self.a.sort(key=lambda x: x.get_data(), reverse=True)

    def __str__(self):
        outstr = "Heap (Size: " + str(len(self.a)) + ")\n"
        level = 0
        outstr = outstr + "Level " + str(level) + ": "
        for i in range(len(self.a)):
            if len(self.a) == 1:
                outstr = outstr + str(self.a[i].get_data())
            elif (i == (2 ** (level + 1) - 2)) and (i != len(self.a) - 1):
                outstr = outstr + str(self.a[i].get_data()) + "\n"
                level = level + 1
            elif i == (2**level) - 1:
                outstr = (
                    outstr
                    + "Level "
                    + str(level)
                    + ": "
                    + str(self.a[i].get_data())
                    + " "
                )
            else:
                outstr = outstr + str(self.a[i].get_data()) + " "
        return outstr


item_list = [4, 32, 1, 11]
myheap = minBHeap()
for item in item_list:
    myheap.Insert(item)
myheap.Sort()
print(myheap)


item_list = ["Peach", "Apple", "Banana", "Orange", "Pear"]
myheap = minBHeap()
for item in item_list:
    myheap.Insert(item)
myheap.Sort()
print(myheap)
