class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answers: List[str] = []
        answer: str = ''
        letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        #answers.clear()
        if not digits:
            return []

        def backtracking(digits: str, index: int) -> None:
            # 回溯函数没有返回值
            # Base Case
            nonlocal answer

            if index == len(digits):  # 当遍历穷尽后的下一层时
                answers.append(answer)
                return
                # 单层递归逻辑
            letters = letter_map[digits[index]]

            for letter in letters:
                answer += letter  # 处理
                backtracking(digits, index + 1)  # 递归至下一层
                answer = answer[:-1]  # 回溯

        backtracking(digits, 0)
        return answers