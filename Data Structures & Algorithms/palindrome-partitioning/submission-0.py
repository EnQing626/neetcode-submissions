class Solution:
    def partition(self, s: str) -> List[List[str]]:
        paths = []
        path = []
        path.clear()
        paths.clear()
        def is_palindrome(s: str, start: int, end: int) -> bool:
            i: int = start
            j: int = end
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def backtracking(s: str, start_index: int) -> None:
            # Base Case
            if start_index >= len(s):
                paths.append(path[:])
                return
            # 单层递归逻辑
            for i in range(start_index, len(s)):
                # 此次比其他组合题目多了一步判断：
                # 判断被截取的这一段子串([start_index, i])是否为回文串
                if is_palindrome(s, start_index, i):
                    path.append(s[start_index:i + 1])
                    backtracking(s, i + 1)  # 递归纵向遍历：从下一处进行切割，判断其余是否仍为回文串
                    path.pop()  # 回溯
                else:
                    continue

        backtracking(s, 0)
        return paths