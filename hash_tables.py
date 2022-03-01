class HashTables:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, value in enumerate(self.data_map):
            print(f"index={i}, val={value}")

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys


ht = HashTables()
ht.print_table()
print("-------------------- set ops-------------------------")
ht.set_item('nails', 6)
ht.set_item('bolt', 5)
ht.set_item('nuts', 9)
print("-------------After set ops----------------------------")
ht.print_table()
print("--------------- Get item ops -------------------------")
print("key = 'nails'")
print(ht.get_item('nails'))
print("key = 'bolts'")
print(ht.get_item('bolts'))
print("key = 'bolt'")
print(ht.get_item('bolt'))
print("key = 'nuts'")
print(ht.get_item('nuts'))
print("--------------------keys ops---------------------------")
print(ht.keys())
print("-------------------- set ops-------------------------")
print("-------------------- set ops for washers key-------------------------")
ht.set_item('washers', 20)
print("--------------------------- keys ops-------------------------")
print(ht.keys())
