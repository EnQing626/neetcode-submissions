from functools import cache
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_end = False
class Trie:
    def __init__(self):
        self.head = TrieNode()
    def insert(self, s: str):
        cur = self.head
        for c in s:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end = True
    def search(self, s: str) -> List[int]:
        ans = []
        cur = self.head
        for i, c in enumerate(s):
            if c not in cur.children:
                break
            cur = cur.children[c]
            if cur.is_end:
                ans.append(i+1)
        return ans
class Solution:
    def minExtraChar(self, s: str, d: List[str]) -> int:
        N = len(s)
        trie = Trie()
        for w in d:
            trie.insert(w)
        @cache
        def dfs(i: int) -> int:
            if i == N:
                return 0
            ans = dfs(i+1) + 1
            for l in trie.search(s[i:]):
                ans = min(ans, dfs(i+l))
            return ans
        return dfs(0)
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        N = len(s)
        trie = Trie()
        for w in dictionary:
            trie.insert(w)
        @cache
        def dfs(i: int) -> int:
            if i == N:
                return 0
            ans = dfs(i+1) + 1
            for l in trie.search(s[i:]):
                ans = min(ans, dfs(i+l))
            return ans
        return dfs(0)