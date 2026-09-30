class Solution:
    def addTwoNumbers(self, head1, head2):
        curr1=head1
        curr2=head2
        
        ans=ListNode(-1)
        c=0
        curr3=ans
        while curr1!=None or curr2 !=None:
            total=c
            c=0
            if curr1 !=None:
                total +=curr1.val
                curr1=curr1.next
            if curr2 !=None:
                total +=curr2.val
                curr2=curr2.next

            if total>9:
                c=1
                total -=10
            newNode=ListNode(total)
            curr3.next=newNode

            curr3 = curr3.next

        if c>0:
            newNode=ListNode(c)
            curr3.next=newNode
        return ans.next

