class Node:

    def __init__(self, init_data):
        self.data = init_data
        self.left = None
        self.right = None

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_left(self):
        return self.left

    def set_left(self, new_next):
        self.left = new_next

    def get_right(self):
        return self.right

    def set_right(self, new_next):
        self.right = new_next


class BST:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def Insert(self, item):
        node = Node(item)
        if self.is_empty():
            self.root = node
        else:
            curr_node = self.root
            while True:
                if item < curr_node.get_data():
                    if curr_node.get_left() == None:
                        curr_node.set_left(node)
                        break
                    else:
                        curr_node = curr_node.get_left()
                else:
                    if curr_node.get_right() == None:
                        curr_node.set_right(node)
                        break
                    else:
                        curr_node = curr_node.get_right()

    def FindMax(self):
        curr_node = self.root
        while curr_node.get_right():
            curr_node = curr_node.get_right()
        return curr_node.get_data()

    def FindMin(self):
        curr_node = self.root
        while curr_node.get_left():
            curr_node = curr_node.get_left()
        return curr_node.get_data()

    def Find(self, item):
        curr_node = self.root
        while curr_node:
            if curr_node.get_data() == item:
                return True
            elif item < curr_node.get_data():
                curr_node = curr_node.get_left()
            else:
                curr_node = curr_node.get_right()
        return False

    def DFS(self, a, current, index):
        if current == None:
            return a
        else:
            parent = current
            current = parent.get_left()
            l_index = index * 2 + 1
            a = self.DFS(a, current, l_index)
            current = parent.get_right()
            r_index = index * 2 + 2
            a = self.DFS(a, current, r_index)
            a[index] = parent.get_data()
        return a

    def __str__(self):
        if self.is_empty():
            return "BST is Empty"
        else:
            a = [None] * 57
            a = self.DFS(a, self.root, 0)
        outstr = "Binary Search Tree\n"
        level = 0
        outstr = outstr + "Level " + str(level) + ": "
        if len(a) > 1:
            for i in range(len(a)):
                if (i == (2 ** (level + 1) - 2)) and (i != len(a) - 1):
                    outstr = outstr + str(a[i]) + "\n"
                    level = level + 1
                else:
                    if i == (2**level) - 1:
                        outstr = outstr + "Level " + str(level) + ": " + str(a[i]) + " "
                    else:
                        outstr = outstr + str(a[i]) + " "
            return outstr


item_list = ["H", "D", "A", "F", "L", "R"]
myBST = BST()
for item in item_list:
    myBST.Insert(item)
print("Find F: " + str(myBST.Find("F")))
print("Find O: " + str(myBST.Find("O")))
print("Find R: " + str(myBST.Find("R")))

item_list = [
    "Japan",
    "China",
    "Brazil",
    "Chile",
    "Germany",
    "Spain",
    "Vietnam",
    "France",
    "Peru",
    "India",
]
myBST = BST()
for item in item_list:
    myBST.Insert(item)
print("Find Spain: " + str(myBST.Find("Spain")))
print("Find China: " + str(myBST.Find("China")))
print("Find Canada: " + str(myBST.Find("Canada")))
