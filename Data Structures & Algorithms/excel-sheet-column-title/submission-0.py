class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        # 10进制 转换为 26进制，A对应1，B对应2,....Z对应26
        while columnNumber > 0:
            # 最右边位为取模运算的结果
            columnNumber -= 1
            # A的ASC码 65
            ans.append(chr(columnNumber%26 + 65))
            columnNumber //= 26
        return ''.join(ans[::-1])