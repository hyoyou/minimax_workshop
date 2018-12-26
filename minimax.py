import unittest

class TreeNode:
    def __init__(self, score=None, children=[]):
        self.score = score
        self.children = children

    def add_child(self, child):
        self.children.append(child)

class MinimaxWorkshop:
    def score(self, node):
        if node.score == None:
            return self.score(node.children[0])
        else:
            return node.score

class TestTreeNode(unittest.TestCase):
    def test_itHasADefaultScoreOfNone(self):
        node = TreeNode()
        self.assertTrue(node.score == None)

class TestMinimaxWorkshop(unittest.TestCase):
    def setUp(self):
        self.mm = MinimaxWorkshop()

    def test_itReturnsTheScoreOfANodeWithNoChildren(self):
        node = TreeNode(-1)
        self.assertTrue(self.mm.score(node) == -1)

    def test_itReturnsTheScoreOfANodeWithOneChild(self):
        child = TreeNode(22)
        parent = TreeNode(None, [child])
        self.assertTrue(self.mm.score(parent) == 22)