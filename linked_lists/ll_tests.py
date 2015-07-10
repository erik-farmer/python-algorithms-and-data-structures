import unittest
from ll import Node
from ll import UnorderedList


class TestNodeInit(unittest.TestCase):

    node = Node('data')

    def test_no_data_node_fails_initialization(self):
        with self.assertRaises(TypeError):
            node = Node()

    def test_node_data_is_set(self):
        self.assertEqual(self.node.data, 'data')

    def test_node_next_is_set(self):
        self.assertEqual(self.node.next, None)


class TestUnorderedList(unittest.TestCase):

    def test_empty_ul_method_returns_true(self):
        ul = UnorderedList()
        self.assertEqual(ul.is_empty(), True)

    def test_addition_of_first_node(self):
        ul = UnorderedList()
        ul.add(Node('first'))
        self.assertEqual(ul.head.data, 'first')

    def test_second_node_addition_moves_head(self):
        ul = UnorderedList()
        ul.add(Node('first'))
        first_head = ul.head
        ul.add(Node('second'))
        second_head = ul.head
        self.assertNotEqual(first_head, second_head)

    def test_size_returns_correct_qty(self):
        ul = UnorderedList()
        ul.add(Node('first'))
        self.assertEqual(ul.size(), 1)
        ul.add(Node('second'))
        self.assertEqual(ul.size(), 2)

    def test_size_new_nodes_are_head(self):
        ul = UnorderedList()
        ul.add(Node('first'))
        self.assertEqual(ul.head.data, 'first')
        ul.add(Node('second'))
        self.assertEqual(ul.head.data, 'second')
        self.assertEqual(ul.head.next.data, 'first')

    def test_search_works_with_zero_to_multiple(self):
        ul = UnorderedList()
        self.assertEqual(ul.search('first'), None)
        first_node = Node('first')
        ul.add(first_node)
        self.assertEqual(ul.search('first'), first_node)
        second_first = Node('first')
        ul.add(second_first)
        self.assertEqual(ul.search('first'), second_first)

    def test_remove(self):
        ul = UnorderedList()
        ul.add(Node('first'))
        ul.add(Node('second'))
        ul.add(Node('third'))
        self.assertEqual(ul.head.next.data, 'second')
        ul.remove('second')
        self.assertEqual(ul.head.next.data, 'first')


if __name__ == '__main__':
    unittest.main()
