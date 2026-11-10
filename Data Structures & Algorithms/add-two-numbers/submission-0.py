# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        # 第二种情况，可以正常相加。考虑进位。
        carry = 0
        dummy = ListNode(0)
        p = dummy
        while l1 and l2:
            p.next = ListNode((l1.val + l2.val + carry) % 10)  # 取余
            carry = (l1.val + l2.val + carry) // 10  # 取整
            l1 = l1.next
            l2 = l2.next
            p = p.next
        # 第三种情况，l1比较短，或者l2比较短。那么除了上面共同位相加，
        # 还要加上剩余位。
        if l1:
            while l1:
                p.next = ListNode((l1.val + carry) % 10)
                carry = (l1.val + carry) // 10
                l1 = l1.next
                p = p.next
        if l2:
            while l2:
                p.next = ListNode((l2.val + carry) % 10)
                carry = (l2.val + carry) // 10
                l2 = l2.next
                p = p.next

        # 第四种情况，最后一位是否包含进位。
        if carry == 1:
            p.next = ListNode(1)

        return dummy.next