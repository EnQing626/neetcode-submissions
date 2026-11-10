class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK1 = 4294967296  # 2^32
        MASK2 = 2147483648  # 2^31
        MASK3 = 2147483647  # 2^31-1

        a%=MASK1
        b%=MASK1

        while b!=0:
            carry=((a&b) << 1)%MASK1
            a=(a^b)%MASK1
            b=carry
        #return a
        if a & MASK2:  # 负数&=MASK2,正数=0
            return ~((a ^ MASK2) ^ MASK3)
        else:  # 正数
            return a