class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1        # 第 n 个数对应填入的数值是 n - 1
        ans = x       # 基础值包含 x 的所有 1
        
        for i in range(31):
            # 1. 判断 x 从右数第 i 位是否为 0
            # x >> i & 1 提取第 i 位；^ 1 表示逻辑取反（是 0 则变成 1，触发 if）
            if x >> i & 1 ^ 1:
                # 2. 把 n 的最低位 (n & 1) 放到 ans 的第 i 位上
                ans |= (n & 1) << i
                # 3. n 右移一位，准备填下一个二进制位
                n >>= 1
                
        # 4. 如果 31 位处理完了 n 还有剩余的位，直接拼接到更高的位置（第 31 位及以上）
        ans |= n << 31
        return ans