# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def insertIntoBST(self, root, val):
        newNode = TreeNode(val)

        if root == None:
            return newNode

        curr = root

        while curr != None:
            if val < curr.val:
                if curr.left != None:
                    curr = curr.left
                else:
                    curr.left = newNode
                    break
            else:
                if curr.right != None:
                    curr = curr.right
                else:
                    curr.right = newNode
                    break

        return root

            
        