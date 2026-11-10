class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def __swap(nums, index1, index2):
            nums[index1],nums[index2]=nums[index2],nums[index1]
        size=len(nums)
        for i in range(len(nums)):
            while 1 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
                __swap(nums, i, nums[i] - 1)
        for i in range(size):
            if i + 1 != nums[i]:
                return i + 1

        return size + 1