from graph import UndirectedGraph
from graph import DirectedGraph
import unittest


class TestDirectedGraph(unittest.TestCase):

    def setUp(self):
        self.dgraph = DirectedGraph()

    def test_single_insertion(self):
        self.dgraph.insert('X', 'Y')
        self.assertEqual(self.dgraph['X'], ['Y'])

    def test_removal_of_existing_node(self):
        self.dgraph = DirectedGraph()
        self.dgraph.insert('D', 'E')
        self.assertEqual(self.dgraph.remove('D'), True)

    def test_removal_of_nonexistent_node(self):
        self.assertEqual(self.dgraph.remove('Foo'), False)


class TestUndirectedGraph(unittest.TestCase):

    def setUp(self):
        self.ugraph = UndirectedGraph()

    def test_single_insertion(self):
        self.ugraph.insert('A', 'B')
        self.assertEqual(self.ugraph['A'], ['B'])
        self.assertEqual(self.ugraph['B'], ['A'])

    def test_removal_of_existing_node(self):
        self.ugraph.insert('X', 'Y')
        self.assertEqual(self.ugraph.remove('Y'), True)

    def test_removal_of_nonexistent_node(self):
        self.assertEqual(self.ugraph.remove('Z'), False)

if __name__ == '__main__':
    unittest.main()