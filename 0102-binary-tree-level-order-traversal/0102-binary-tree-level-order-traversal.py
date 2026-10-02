
class Queue:
    def __init__(self):
        self.q = []
        self.front = -1

    def push(self, x):
        if self.front == -1:
            self.front = 0
        self.q.append(x)

    def pop(self):
        if self.front == -1:
            return -1

        x = self.q[self.front]
        self.front += 1

        if self.front == len(self.q):
            self.front = -1
            self.q = []

        return x

    def getFront(self):
        if self.front == -1:
            return -1
        return self.q[self.front]

    def size(self):
        if self.front == -1:
            return 0
        return len(self.q) - self.front


class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []

        queue = Queue()
        ans = []

        queue.push(root)

        while queue.size() > 0:
            l = queue.size()
            level = []

            for i in range(l):
                front = queue.pop()
                level.append(front.val)

                if front.left is not None:
                    queue.push(front.left)

                if front.right is not None:
                    queue.push(front.right)

            ans.append(level)

        return ans
