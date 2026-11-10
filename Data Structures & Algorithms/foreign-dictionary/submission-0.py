class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Step 1: 构建邻接表和入度表
        graph = collections.defaultdict(set)
        in_degree = {char: 0 for word in words for char in word}

        # Step 2: 比较相邻单词，确定字母顺序
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_length = min(len(word1), len(word2))

            # 检查无效输入（前缀问题）
            if word1.startswith(word2) and len(word1) > len(word2):
                return ""

            # 找到第一个不同的字符
            for j in range(min_length):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]:  # 避免重复边
                        graph[word1[j]].add(word2[j])
                        in_degree[word2[j]] += 1
                    break

        # Step 3: BFS 拓扑排序
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        result = []

        while queue:
            char = queue.popleft()
            result.append(char)
            for neighbor in graph[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: 检查是否有环（拓扑排序结果必须包含所有字母）
        return "".join(result) if len(result) == len(in_degree) else ""