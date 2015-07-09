class UnorderedList(object):

    def __init__(self):
        self.head = None

    def add(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def is_empty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def search(self, data):
        current = self.head
        while current is not None and current.data != data:
            current = current.next
        return current

    def remove(self, data):
        previous, current = None, self.head
        while current is not None:
            if current.data == data:
                break
            previous, current = current, current.next
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None
