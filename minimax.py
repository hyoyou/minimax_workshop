import unittest

class TreeNode:
    def __init__(self, score=None, children=[]):
        self.score = score
        self.children = children

class MinimaxWorkshop:
    def score(self, node, level=0):
        if node.score == None:
            result = []
            for child in node.children: 
                result.append(self.maximize(child, level+1))
            return max(result)
        else:
            return node.score

    def maximize(self, node, level=0):
        if node.score == None:
            result = []
            for child in node.children: 
                result.append(self.minimize(child, level+1))
            return min(result)
        else:
            return node.score
    
    def minimize(self, node, level=0):
        if node.score == None:
            result = []
            for child in node.children: 
                result.append(self.maximize(child, level+1))
            return max(result)
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

    def test_itReturnsTheScoreOfAGameWithOneMoveAndTwoPossibleEndStates(self):
        child_one = TreeNode(0)
        child_two = TreeNode(1)
        parent = TreeNode(None, [child_one, child_two])
        self.assertTrue(self.mm.score(parent) == 1)
    
    def test_itReturnsTheScoreOfAGameWithThreeMovesWhereOnlyTheMaximizerGetsToMove(self):
        leaf_1 = TreeNode(11)
        leaf_2 = TreeNode(10)
        leaf_3 = TreeNode(22)
        leaf_4 = TreeNode(-5000)
        grandchild_1 = TreeNode(None, [leaf_1, leaf_2])
        grandchild_2 = TreeNode(None, [leaf_3, leaf_4])
        child_one = TreeNode(None, [grandchild_1])
        child_two = TreeNode(None, [grandchild_2])
        parent = TreeNode(None, [child_one, child_two])
        self.assertTrue(self.mm.score(parent) == 22)

    def test_itReturnsTheScoreForADeeplyNestedGame(self):
        leaf_1 = TreeNode(1)
        leaf_2 = TreeNode(-2)
        leaf_3 = TreeNode(2)
        leaf_4 = TreeNode(-5)
        leaf_5 = TreeNode(-11)
        leaf_6 = TreeNode(-30)
        leaf_7 = TreeNode(20)
        leaf_8 = TreeNode(51)
        leaf_9 = TreeNode(12)
        leaf_10 = TreeNode(10)
        leaf_11 = TreeNode(6)
        leaf_12 = TreeNode(7)
        leaf_13 = TreeNode(8)
        leaf_14 = TreeNode(9)
        leaf_15 = TreeNode(3)
        leaf_16 = TreeNode(4)
        leaf_17 = TreeNode(7)
        leaf_18 = TreeNode(5)
        leaf_19 = TreeNode(9)
        leaf_20 = TreeNode(11)
    
        level4_a = TreeNode(None, [leaf_1, leaf_2])
        level4_b = TreeNode(None, [leaf_3, leaf_4])
        level4_c = TreeNode(None, [leaf_5, leaf_6])
        level4_d = TreeNode(None, [leaf_7, leaf_8])
        level4_e = TreeNode(None, [leaf_9, leaf_10])
        level4_f = TreeNode(None, [leaf_11, leaf_12])
        level4_g = TreeNode(None, [leaf_13, leaf_14])
        level4_h = TreeNode(None, [leaf_15, leaf_16])
        level4_i = TreeNode(None, [leaf_17, leaf_18])
        level4_j = TreeNode(None, [leaf_19, leaf_20])
    
        level3_a = TreeNode(None, [level4_a, level4_b])
        level3_b = TreeNode(None, [level4_c, level4_d])
        level3_c = TreeNode(None, [level4_e, level4_f])
        level3_d = TreeNode(None, [level4_g, level4_h])
        level3_e = TreeNode(None, [level4_i, level4_j])
        level3_f = TreeNode(1)
        level3_g = TreeNode(2)
        level3_h = TreeNode(61)
    
        level2_a = TreeNode(None, [level3_a, level3_b])
        level2_b = TreeNode(None, [level3_c, level3_d])
        level2_c = TreeNode(None, [level3_e, level3_f])
        level2_d = TreeNode(None, [level3_g, level3_h])
    
        level1_a = TreeNode(None, [level2_a, level2_b])
        level1_b = TreeNode(None, [level2_c, level2_d])
    
        root = TreeNode(None, [level1_a, level1_b])
        self.assertTrue(self.mm.score(root) == 7)