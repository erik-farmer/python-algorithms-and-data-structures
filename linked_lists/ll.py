class UnorderedList(object):

    def __init__(self):
        self.head = None

    def add(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def is_empty(self):
        return self.head is None


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None
