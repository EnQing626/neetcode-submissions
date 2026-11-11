# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def listnode_to_list(self,node):
        res = []
        current = node
        while current:
            res.append(current.val)  # 假设节点的值属性是 val
            current = current.next
        return res
    def reorderList(self, head: Optional[ListNode]) -> None:
        from collections import deque
        que=deque()
        temp=head
        while temp.next:
            que.append(temp.next)
            temp=temp.next
        temp=head
        # 把 deque 里的每个链表都展开成普通的 Python 列表
# 遍历 deque，打印每一个链表的内容
        # for i, head in enumerate(que):
        #     print(f"第 {i} 个链表: {self.listnode_to_list(head)}")
        while len(que):
            temp.next=que.pop()
            temp=temp.next
            print('enter:'+str(len(que)))
            if len(que):
                temp.next=que.popleft()
                temp=temp.next
        temp.next=None