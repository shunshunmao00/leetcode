# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root
        self.count = 0
        self.function(root)

        return root

    def function(self, treeNode):
        if treeNode.right != None:
            self.function(treeNode.right)
        treeNode.val += self.count
        self.count = treeNode.val
        if treeNode.left != None:
            self.function(treeNode.left)




if __name__ == "__main__":
    def showTree(tree):
        if tree == None:
            return
        print( tree.val)
        showTree(tree.left)
        showTree(tree.right)

    solution = Solution()
    t1 = None
    # t1 = TreeNode(5)
    # print(t1)
    # t1.left = TreeNode(2)
    # t1.right = TreeNode(13)
    #
    # showTree(t1)

    solution.convertBST(t1)
    showTree(t1)