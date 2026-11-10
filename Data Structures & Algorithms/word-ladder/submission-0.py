class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def judge(s1, s2):
            count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    count += 1
            return count == 1

        n=len(wordList)
        if endWord not in wordList:
            return 0

        # use bfs
        visit = [False for i in range(n)]
        queue = [[beginWord, 1]]
        while queue:
            str, step = queue.pop(0)
            if judge(str, endWord):
                return step+1
            for i in range(n):
                if visit[i] == False and judge(wordList[i], str):
                    visit[i] = True
                    queue.append([wordList[i], step + 1])
        return 0