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
            return self.maximize(node.children[0])
        else:
            return node.score

    def maximize(self, node):
        if node.score == None:
            scores = []
            for child in node.children:
                scores.append(child.score)
            return min(scores)
        else:
            return node.score
    
    def minimize(self, node):
        if node.score == None:
            return self.maximize(node.children[0])
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
    
    def test_itReturnsTheScoreOfALinkedListOfNodes(self):
        grandchild = TreeNode(17)
        child = TreeNode(None, [grandchild])
        parent = TreeNode(None, [child])
        self.assertTrue(self.mm.score(parent) == 17)
    
    def test_itReturnsTheScoreOfAGameWithTwoMovesAndTwoPossibleEndStates(self):
        grandchild_one = TreeNode(1)
        grandchild_two = TreeNode(0)
        child = TreeNode(None, [grandchild_one, grandchild_two])
        parent = TreeNode(None, [child])
        self.assertTrue(self.mm.score(parent) == 0)

    def test_itReturnsTheScoreOfAGameWithTwoMovesAndThreePossibleEndStates(self):
        grandchild_one = TreeNode(12)
        grandchild_two = TreeNode(-10)
        grandchild_three = TreeNode(4)
        child = TreeNode(None, [grandchild_one, grandchild_two, grandchild_three])
        parent = TreeNode(None, [child])
        self.assertTrue(self.mm.score(parent) == -10)