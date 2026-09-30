class Solution(object):
    def removeNthFromEnd(self, head, n):

        length = 0
        curr = head

        # Find length
        while curr:
            length += 1
            curr = curr.next

        if n == length:
            return head.next

        curr = head

        for i in range(length - n - 1):
            curr = curr.next
            
        curr.next = curr.next.next

        return head