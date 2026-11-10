class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right = 0
        res = 0
        left = 0
        window = {}

        while right < len(s):
            #增大窗口
            c1 = s[right]
            window[c1] = window.get(c1, 0) + 1
            right += 1

            #缩小窗口
            while window[c1] > 1:
                c2 = s[left]
                window[c2] -= 1
                left += 1
            res = max(res, right - left)
        return res