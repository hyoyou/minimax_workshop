import unittest

class TreeNode:
    def __init__(self, score=None, children=[]):
        self.score = score
        self.children = children

class MinimaxWorkshop:
    def score(self, node):
        if node.score == None:
            result = []
            for child in node.children: 
                result.append(self.maximize(child))
            return max(result)
        else:
            return node.score

    def maximize(self, node):
        if node.score == None:
            result = []
            for child in node.children: 
                result.append(self.score(child))
            return min(result)
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
    
    def test_itReturnsTheScoreOfAGameWithFourMovesAndOnlyTheMinimizerGetsToMove(self):
        leaf_1 = TreeNode(1)
        leaf_2 = TreeNode(0)
        leaf_3 = TreeNode(2)
        leaf_4 = TreeNode(-5)
        node_level3_a = TreeNode(None, [leaf_1, leaf_2])
        node_level3_b = TreeNode(None, [leaf_3, leaf_4])
        grandchild_1 = TreeNode(None, [node_level3_a])
        grandchild_2 = TreeNode(None, [node_level3_b])
        child = TreeNode(None, [grandchild_1, grandchild_2])
        parent = TreeNode(None, [child])
        self.assertTrue(self.mm.score(parent) == -5)