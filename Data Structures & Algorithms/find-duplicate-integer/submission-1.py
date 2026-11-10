class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]  # 类比链表slow=slow.next
            fast = nums[nums[fast]]  # 类比链表fast=fast.next.next
            if fast == slow:  # 首次相遇点
                break

        fast = 0  # fast回到起点
        while slow != fast:  # 再次相遇点即为重复数字
            slow = nums[slow]
            fast = nums[fast]

        return fast