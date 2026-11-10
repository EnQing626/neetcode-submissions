class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        used = [[False] * n for _ in range(m)]
        
        def dfs(row, col, i): # 判断当前点是否是目标路径上的点. row col 当前点的坐标，i当前考察的word字符索引
            if i == len(word): # 递归结束条件 : 找到了单词的最后一个
                return True
            if row < 0 or row >= m or col < 0 or col >= n: # 越界
                return False
            if used[row][col] or board[row][col] != word[i]:# 已经访问过,或者不是word里的字母
                return False
            # 排除掉上面的false情况，当前点是合格的，可以继续递归考察
            used[row][col] = True #  记录一下当前点被访问了
            if dfs(row+1, col, i+1) or dfs(row-1, col, i+1) or dfs(row, col+1, i+1) or dfs(row, col-1, i+1): # 基于当前点[row,col]，可以为剩下的字符找到路径
                return True
            used[row][col] = False # 不能为剩下字符找到路径，返回false，撤销当前点的访问状态，继续考察别的分支
            return False


        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False