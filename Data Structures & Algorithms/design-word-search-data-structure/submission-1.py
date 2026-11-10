class WordDictionary:

    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def addWord(self, word) -> None:
        node = self
        for ch in word:
            idx = ord(ch) - ord("a")
            if not node.children[idx]:
                node.children[idx] = WordDictionary()
            node = node.children[idx]
        node.isEnd = True

    def search(self, word) -> bool:
        return self._search(word, 0)

    def _search(self, word, index: int) -> bool:
        if index == len(word):
            return self.isEnd

        ch = word[index]
        if ch == '.':
            # 尝试所有可能的子节点
            for child in self.children:
                if child and child._search(word, index + 1):
                    return True
            return False
        else:
            idx = ord(ch) - ord("a")
            child = self.children[idx]
            if not child:
                return False
            return child._search(word, index + 1)