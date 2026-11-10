# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n # [1,2]

        # 最后只剩一个数 极端情况 但是left肯定不会比right大
        while left <= right:
            mid = (left+right) // 2

            # 猜的是中间的数 mid不对要偏左或者偏右
            result = guess(mid)

            if result == 0:
                return mid
            elif result == -1:
                right = mid-1
            else: 
                left = mid+1