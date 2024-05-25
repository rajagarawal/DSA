class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_index(self, index, value):
        if index < 0:
            raise IndexError("Index out of range")
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete_index(self, index):
        if index < 0 or self.head is None:
            raise IndexError("Index out of range")
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for i in range(index - 1):
            if current.next is None:
                raise IndexError("Index out of range")
            
            current = current.next
        if current.next is None:
                raise IndexError("Index out of range")
        current.next = current.next.next

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def is_empty(self):
        return self.head is None

    def rotate_ktimes(self, k):
        if self.head is None or k == 0:
            return
        len = self.size()
        k = k % len
        if k == 0:
            return
        prev = None 
        current = self.head
        for i in range(len- k):
            prev = current
            current = current.next
        prev.next = None
        new_head = current
        while current.next:
            current = current.next
            current.next = self.head
            self.head = new_head

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def merge(self, other):
        if self.head is None:
            self.head = other.head
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = other.head

    

    def middle_ele(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow:
                return slow.value
            else:
                None
        

    def index(self, value):
        index = 0
        current = self.head
        while current:
            if current.value == value:
                return index
            index += 1
            current = current.next
        return -1

    def split_by_index(self, index):
        if index < 0:
            raise IndexError("Index out of range")
        if index == 0:
            second_half = self.head
            self.head = None
            return LinkedList(), second_half
        current = self.head
        for _ in range(index - 1):
            if current.next is None:
                raise IndexError("Index out of range")
            current = current.next
        second_half = current.next
        current.next = None
        return self, second_half
my_list=LinkedList()
