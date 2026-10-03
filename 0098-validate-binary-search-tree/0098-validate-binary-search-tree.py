# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def check(self,root,mn,mx):
        if root is None:
            return True
        if root.val<mn or root.val>mx:
            return False

        checLeft=self.check(root.left,mn,root.val-1)
        checkRight=self.check(root.right,root.val+1,mx)

        return checLeft and checkRight
        
    def isValidBST(self, root):
        return self.check(root,float('-inf'), float('inf'))

         
        