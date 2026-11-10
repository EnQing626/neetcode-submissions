"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        d=dict()
        p=head
        while p:
            p_new=Node(p.val,None,None)
            d[p]=p_new
            p=p.next
        p=head
        while p:
            if p.next:
                d[p].next=d[p.next]
            if p.random:
                d[p].random=d[p.random]
            p=p.next
        return d[head]