class Node:

    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class FirstList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        curr = self.head
        count = 0
        while curr != None:
            count = count + 1
            curr = curr.get_next()
        return count

    def addinOrder(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
        else:
            curr = self.head
            prev = None
            while curr and curr.get_data() > node.get_data():
                prev = curr
                curr = curr.get_next()
            if prev:
                prev.set_next(node)
                node.set_next(curr)
            else:
                node.set_next(curr)
                self.head = node

    def add(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node

    def __str__(self):
        current = self.head
        previous = None
        found = False
        outstr = "["
        while current != None:
            if current.get_next() == None:
                outstr = outstr + str(current.get_data())
            else:
                outstr = outstr + str(current.get_data()) + " "
            current = current.get_next()
        outstr = outstr + "]"
        return outstr


name_list = [44, 32, 31, 21, 33]
my_orderedlist = FirstList()
for number in name_list:
    my_orderedlist.addinOrder(number)
print(my_orderedlist)

name_list = ["Gill", "Tom", "Eduardo", "Raffaele", "Serena", "Bella"]
my_orderedlist = FirstList()
for name in name_list:
    my_orderedlist.addinOrder(name)
print(my_orderedlist)
