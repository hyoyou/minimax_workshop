import unittest

class TreeNode:
    def __init__(self):
        self.score = None
        self.children = []

class TestTreeNode(unittest.TestCase):
    def test_itHasADefaultScoreOfNone(self):
        node = TreeNode()
        self.assertTrue(node.score == None)