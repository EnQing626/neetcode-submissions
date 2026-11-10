# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        import collections
        d = collections.deque()
        tmp = head
        while tmp.next: # 链表除了首元素全部加入双向队列
            d.append(tmp.next)
            tmp = tmp.next
        tmp = head
        while len(d): # 一后一前加入链表
            tmp.next = d.pop()
            tmp = tmp.next
            if len(d):
                tmp.next = d.popleft()
                tmp = tmp.next
        tmp.next = None # 尾部置空