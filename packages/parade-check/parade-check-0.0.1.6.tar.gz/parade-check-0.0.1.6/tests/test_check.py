import unittest
from src.parade.command.check import check


class TestBaseCase(unittest.TestCase):
    def setUp(self):
        self.flows_a = {
            'A': [],
            'B': ['D'],
            'C': ['C'],
            'D': ['A', 'B', 'A', 'a', 'a', 'A'],
            'E': ['C'],
            'F': ['D', 'e'],
            'G': ['D']
        }

    def test_non_deps(self):
        non_deps, _, _ = check(self.flows_a)
        self.assertEqual({'D': ['a'], 'F': ['e']}, non_deps)

    def test_duplicate_deps(self):
        _, duplicate, _ = check(self.flows_a)
        self.assertIn('D', duplicate)
        self.assertIn(('a', 2), duplicate['D'])
        self.assertIn(('A', 3), duplicate['D'])

    def test_circular_deps(self):
        _, _, circular = check(self.flows_a)
        self.assertIn('B', circular)
        self.assertIn('D', circular['B'][0])
        self.assertIn('C', circular)
        self.assertEqual(['C'], circular['C'])
        self.assertIn('D', circular)
        self.assertIn('B', circular['D'][0])
