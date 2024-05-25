class DynamicArray:
    def __init__(self, resize_fact=2):
        self.array = []
        self.resize_fact = resize_fact

    def insert_index(self, index, value):
        if index < 0 or index > len(self.array):
            raise IndexError("Index out of bounds")
        self.array.insert(index, value)

    def delete_index(self, index):
        if index < 0 or index >= len(self.array):
            raise IndexError("Index out of bounds")
        del self.array[index]

    def get_the_size(self):
        return len(self.array)

    def is_empty(self):
        return len(self.array) == 0


    def reverse(self):
        self.array.reverse()

    def append(self, value):
        self.array.append(value)

    def get_middle_element(self):
        if len(self.array) == 0:
            return None
        mid_index = len(self.array) // 2
        return self.array[mid_index]