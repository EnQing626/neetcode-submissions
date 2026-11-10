class Trie_word_search:
    def __init__(self):
        self.children = defaultdict(Trie_word_search)
        self.word = ""
        self.is_word=False

    def insert(self, word):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.is_word = True
        cur.word = word
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie_word_search()
        for word in words:
            trie.insert(word)

        m, n = len(board), len(board[0])
        ans = set()
        visited = [[False for _ in range(n)] for _ in range(m)]

        def dfs(now, i1, j1):
            if board[i1][j1] not in now.children or visited[i1][j1]:
                return

            ch = board[i1][j1]
            now = now.children[ch]
            #if now.word != "":
            if now.is_word:
                ans.add(now.word)

            visited[i1][j1] = True
            for i2, j2 in [(i1 + 1, j1), (i1 - 1, j1), (i1, j1 + 1), (i1, j1 - 1)]:
                if 0 <= i2 < m and 0 <= j2 < n:
                    dfs(now, i2, j2)
            visited[i1][j1] = False  # 回溯

        for i in range(m):
            for j in range(n):
                dfs(trie, i, j)

        return list(ans)