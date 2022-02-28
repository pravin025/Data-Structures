class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
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
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return 0
        if index < self.length / 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.next = after
        new_node.prev = before

        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.prev = None
        temp.next = None
        self.length -= 1
        return temp


print("------------------------- dll -------------------------")
d_ll = DoublyLinkedList(7)
d_ll.print_list()
print("---------------------------Append ops --------------------")
d_ll.append(12)
d_ll.print_list()
d_ll.append(3)
d_ll.append(19)
d_ll.append(8)
print("-----------------------------print list ops-----------------------------------")
d_ll.print_list()
print("----------------------------- pop ops ------------------------------------------")
print("--------------------------Before pop ops ---------------------------------------")
d_ll.print_list()
d_ll.pop()
print("-------------------------Afetr pop ops ---------------------------------")
d_ll.print_list()
# print("---------------------- No ele in dll ------------------------------")
# empty_ll = DoublyLinkedList(None)
# print("--------------------------Before pop ops ---------------------------------------")
# empty_ll.print_list()
# empty_ll.pop()
# print("-------------------------Afetr pop ops ---------------------------------")
# empty_ll.print_list()
print("---------------------- Single ele in dll ------------------------------")
s_ll = DoublyLinkedList(7)
print("--------------------------Before pop ops ---------------------------------------")
s_ll.print_list()
s_ll.pop()
print("-------------------------Afetr pop ops ---------------------------------")
s_ll.print_list()
print("------------------------Prepend ops ----------------------------")
d_ll = DoublyLinkedList(7)
d_ll.append(8)
print("-----------------Before ops ------------------------")
d_ll.print_list()
print("--------------------------After ops ------------------------")
d_ll.prepend(9)
print(d_ll.print_list())
print("---------------------------- pop first ops -------------------------")
d_ll = DoublyLinkedList(9)
d_ll.append(7)
print("------------------- before pop first ops ---------------------------------")
d_ll.print_list()
d_ll.pop_first()
print("------------------------ After pop first ops ----------------------------")
d_ll.print_list()
print("------------------- before pop first ops ---------------------------------")
d_ll.print_list()
d_ll.pop_first()
print("------------------------ After pop first ops ----------------------------")
d_ll.print_list()
print("----------------------- Get ops -------------------------------------------")
d_ll = DoublyLinkedList(5)
d_ll.append(9)
d_ll.prepend(10)
d_ll.prepend(11)
d_ll.prepend(12)
d_ll.prepend(13)
print(" Before ops -----------------------------------")
d_ll.print_list()
print(d_ll.get(5).value)
print(d_ll.get(2).value)
print("---------------------------- Insert Ops ------------------------------")
print("before insert----------------------------------------------------------")
d_ll.print_list()
d_ll.insert(3, 22)
d_ll.insert(0, 33)
print("After insert-------------------------------------------------------------")
d_ll.print_list()
print("-------------------------------Remove ops ----------------------------")
print("-----------------------------before ops -------------------------")
d_ll.print_list()
d_ll.remove(0)
print("------------------------ After ops ----------------------------")
d_ll.print_list()
print("-----------------------------before ops -------------------------")
d_ll.print_list()
d_ll.remove(d_ll.length-1)
print("------------------------ After ops ----------------------------")
d_ll.print_list()
print("-----------------------------before ops -------------------------")
d_ll.print_list()
d_ll.remove(2)
print("------------------------ After ops ----------------------------")
d_ll.print_list()
