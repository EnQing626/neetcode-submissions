class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        cnt = 0
        # 找到left和right的公共前缀，并统计这个过程右移了多少次
        while left != right:
            cnt += 1
            left >>= 1
            right >>= 1
        # 将这个公共前缀还原回去
        return (left & right) << cnt