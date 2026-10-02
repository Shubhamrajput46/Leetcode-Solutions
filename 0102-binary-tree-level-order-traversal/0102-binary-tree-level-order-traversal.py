# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []

        q = [root]
        ans = []

        while q:
            level = []
            size = len(q)

            for i in range(size):
                curr = q.pop(0)
                level.append(curr.val)

                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)

            ans.append(level)

        return ans

        