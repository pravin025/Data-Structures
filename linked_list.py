class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


# my_ll = LinkedList(None)
#
# my_ll.print_list()
# print("--------------------- one element in ll ----------------------")
# my_ll = LinkedList(4)
# print(my_ll.pop().value)
# print("------------ initialization-----------------")
# my_ll = LinkedList(1)
#
# my_ll.print_list()
#
# print("------------ append operation-----------------")
# my_ll.append(2)
#
# my_ll.print_list()
#
# my_ll.append(5)
# my_ll.append(8)
# my_ll.append(9)
# print("----------------------------------- pop operation ---------------------------------")
# print(my_ll.pop().value)
#
# print("--------------------------- Prepend ------------------------------------------")
# print("------------------------------ 18 -------------------------------------------")
# my_ll.prepend(18)
# my_ll.print_list()
# print("------------------------------ 22 -------------------------------------------")
# my_ll.prepend(22)
# my_ll.print_list()
#
# print("--------------------------- Pop first -----------------------------------------")
# my_ll.pop_first()
# my_ll.print_list()
#
# print("___________________________ only on element ------------------------------------")
# single_ll = LinkedList(5)
# single_ll.pop_first()
# single_ll.print_list()
#
# print("-------------------------- No ele in list ---------------------------------------")
# empty_ll = LinkedList(None)
# empty_ll.pop_first()
# empty_ll.print_list()
#
# print("-------------------------- get ---------------------------------------------------")
# get_ll = LinkedList(5)
# get_ll.append(8)
# get_ll.prepend(9)
# get_ll.prepend(12)
# get_ll.prepend(5)
# get_ll.prepend(44)

# get_ll = [44, 5, 12, 9, 5, 8]

# print("---------------------------- get ops ----------------------------------------------")
# print("---------------------------- at 0 index --------------------------------------------")
# print(get_ll.get(0))
# print("---------------------------- at invalid index --------------------------------------------")
# print(get_ll.get(10))
# print(get_ll.get(-1))
# print("---------------------------- at middle index index --------------------------------------------")
# print(get_ll.get(0))
#
# print("------------------------------ set value ----------------------------------------------------")
# print("-----------------------set value when ll is empty--------------------------------------------")
# empty_ll = LinkedList(None)
# print("--------------------- ll before set value ----------------------------------------------------")
# print(empty_ll.print_list())
# empty_ll.set_value(0, 10)
# print("---------------------ll after set value -------------------------------------------------------")
# print(empty_ll.print_list())
# print("-----------------------set value on single ele ll--------------------------------------------")
# empty_ll = LinkedList(5)
# print("--------------------- ll before set value ----------------------------------------------------")
# print(empty_ll.print_list())
# empty_ll.set_value(0, 10)
# print("---------------------ll after set value -------------------------------------------------------")
# print(empty_ll.print_list())
#
# print("--------------------- insert ops --------------------------------------------------------------")
# my_ll = LinkedList(8)
# my_ll.append(7)
# my_ll.prepend(17)
# my_ll.insert(0, 11)
# print(my_ll.print_list())
# my_ll.insert(2, 22)
# # print(" ---------------------------------- insert 22 at 2nd index ---------------------------------------")
# print(my_ll.print_list())

print("----------------------- Remove ops -------------------------------------------")
rm_ll = LinkedList(8)
rm_ll.append(17)
rm_ll.prepend(66)
rm_ll.insert(1, 1)
print("------------------------------rm_ll before remove ops------------------------------------------")
print(rm_ll.print_list())
rm_ll.remove(0)
print("-------------------------- after ops --------------------------")
print(rm_ll.print_list())

print("--------------------- in valid index-----------------------")
rm_ll.remove(-2)
print("-------------------- At the end ----------------------------")
print("----------------------before ops------------------------------")
print(rm_ll.print_list())
rm_ll.remove(2)
print(" After ops-------------------------------")
print(rm_ll.print_list())
