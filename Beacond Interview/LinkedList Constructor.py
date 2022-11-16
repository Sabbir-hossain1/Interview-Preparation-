# Create a node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Linked list
class LinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    # Append an item to the list
    def append(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        return True

    # Pop item from linked list
    def pop(self):
        if self.length == 0:
            return "List is empty"
        elif self.length == 1:
            value = self.head.value
            self.head = None
            self.tail = None
            return value
        else:
            temp = self.head
            prev = self.head
            while (temp.next):
                prev = temp
                temp = temp.next
            value = temp.value
            self.tail = prev
            self.tail.next = None
            self.length -= 1
            return value

    # Pop the first element of the linked list
    def pop_first(self):
        if self.length == 0:
            return "List is empty"
        elif self.length == 1:
            value = self.head.value
            self.head = None
            self.tail = None
            return value

        else:
            value = self.head.value
            self.head = self.head.next
            self.length -= 1
            return value

    # Get a specific node of linkelist
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    # Set a linked list item
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    # Insert a node at first
    def prepend(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        return True

    # Insert a node to a particular position
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        newNode = Node(value)
        temp = self.get(index - 1)
        newNode.next = temp.next
        temp.next = newNode
        self.length += 1
        return True

    # Remove an item form linked list
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    # Reverse a linked list
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    # Print the linked list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next


object1 = LinkedList('A')
object1.append('B')
object1.append('C')
object1.reverse()
object1.print_list()



