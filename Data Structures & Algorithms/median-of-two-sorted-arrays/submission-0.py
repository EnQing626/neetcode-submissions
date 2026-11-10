class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ## 获取两个数组的长度
        n1 = len(nums1)
        n2 = len(nums2)
        ## 确保nums1是较短的数组，以简化二分查找的边界条件
        if n1 > n2:
            return self.findMedianSortedArrays(nums2,nums1)
        # 计算合并后数组的中位数索引（如果总长度为奇数，则取中间值；如果为偶数，则取中间两个值的平均）
        k = (n1 + n2 + 1)//2
        # 初始化二分查找的边界
        left = 0
        right = n1
        # 进行二分查找以找到合适的分割点
        while left < right :
		        # 计算当前分割点在nums1中的索引
            m1 = left +(right - left)//2
            # 根据总长度和m1计算分割点在nums2中的索引
            m2 = k - m1
            # 如果nums1的当前分割点值小于nums2对应分割点前一个值，则需要移动分割点到右边
            if nums1[m1] < nums2[m2-1]:
                left = m1 + 1
            # 否则，移动分割点到左边
            else:
                right = m1
        # 更新分割点索引
        m1 = left
        m2 = k - m1
        # 计算左半部分最大值（用于确定中位数）
        c1 = max(nums1[m1-1] if m1 > 0 else float("-inf"), nums2[m2-1] if m2 > 0 else float("-inf") )# nums1分割点前一个值（如果存在）# nums2分割点前一个值（如果存在）
        if (n1 + n2) % 2 == 1:
            return c1
        # 如果总长度为偶数，则计算右半部分最小值，并与左半部分最大值取平均作为中位数
        c2 = min(nums1[m1] if m1 < n1 else float("inf"), nums2[m2] if m2 <n2 else float("inf"))
        return (c1 + c2) / 2