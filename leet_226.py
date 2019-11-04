# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root
        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)
        return root


if __name__=="__main__":

    def showTree(tree):
        if tree == None:
            return
        print( tree.val)
        showTree(tree.left)
        showTree(tree.right)


    solution = Solution()
    t1 = TreeNode(1)
    print(t1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(3)
    t1.left.left = TreeNode(4)
    t1.left.right = TreeNode(5)
    # showTree(t1)
    t2 = TreeNode(5)
    t2.left = TreeNode(3)
    t2.right = TreeNode(6)
    t2.left.left = TreeNode(2)
    t2.right.left = TreeNode(1)
    t2.right.right = TreeNode(4)
    showTree(t2)
    t3 = solution.invertTree(t2)
    showTree(t3)