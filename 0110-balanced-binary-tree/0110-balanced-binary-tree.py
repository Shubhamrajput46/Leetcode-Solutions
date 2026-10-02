# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.ans=True

    def height(self, root):
        if root==None:
            return 0

        leftHeight=self.height(root.left)
        rightHeight=self.height(root.right)

        if abs(leftHeight-rightHeight)>1:
            self.ans=False

        return max(leftHeight,rightHeight)+1

    def isBalanced(self, root):
        self.height(root)
        return self.ans
       
        