"""Components needed for a linked list in Python

   TODOS:
        Make it so only Node objects can be added to lists
        Add OrderedList search, remove to account for size
        Add test file
"""


class UnorderedList(object):
    """A basic implementation of the unordered/linked list in Python."""

    def __init__(self):
        self.head = None

    def add(self, new_node):
        """Adds a node to the UnorderedList.

        Args:
            new_node: Node object to be added to the list (becomes list head).
        """
        new_node.next = self.head
        self.head = new_node

    def is_empty(self):
        """Returns a Boolean if the UnorderedList has no Node objects."""
        return self.head is None

    def size(self):
        """Returns the count of Nodes within the UnorderedList."""
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def search(self, data):
        """Searches UnorderedList for Node with data argument.

        Args:
            data: The data attribute of a Node we are searching for within the
                  UnorderedList.

        Returns:
            None object or Node with arg 'data'
        """
        current = self.head
        while current is not None and current.data != data:
            current = current.next
        return current

    def remove(self, data):
        """Changes Node chaining to remove it from the list.

        Args:
            data: Node with data we want removed from chain.
        """
        previous, current = None, self.head
        while current is not None:
            if current.data == data:
                break
            previous, current = current, current.next
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next


class OrderedList(UnorderedList):
    """SubClass of UnorderedList that implements sorting on add"""

    def add(self, new_node):
        """Adds a new_node to the OrderedList taking the data attribute into
           account.
        """
        previous, current = None, self.head
        while current is not None and current.data < new_node.data:
            previous, current = current, current.next
        if previous is None:
            self.head = new_node
        else:
            previous.next = new_node
            new_node.next = current


class Node(object):
    """Node object to be added to an UnorderedList"""

    def __init__(self, data):
        self.data = data
        self.next = None
