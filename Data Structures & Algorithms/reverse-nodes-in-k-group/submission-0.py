# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, tail):#这个过程就是把head的node一个接着一个挪到tail后面
            pre=tail.next
            p=head
            while pre!=tail:
                post=p.next

                p.next=pre
                pre=p
                p=post
            return tail, head

        dummy=ListNode(next=head)
        pre=dummy
        while head:
            tail=pre
            for i in range(k):
                tail=tail.next
                if not tail:
                    return dummy.next
            post=tail.next
            head, tail=reverse(head,tail)
            pre.next=head
            tail.next=post

            head=tail.next
            pre=tail
        return dummy.next