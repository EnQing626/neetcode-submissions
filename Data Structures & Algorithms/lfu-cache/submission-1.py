class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_value_and_freq = {}  # key -> [value, freq]
        # from collections import OrderedDict
        # OrderedDict = dict + 双向链表
        self.freq_to_dict = defaultdict(OrderedDict)  # freq -> OrderedDict（只保存 key）

    def get_list(self, key: int) -> Optional[List[int]]:
        lst = self.key_to_value_and_freq.get(key, None)
        if not lst:  # 没有这本书
            return None
        freq = lst[1]  # 获取这本书在第几摞
        del self.freq_to_dict[freq][key]  # 把这本书抽出来
        if not self.freq_to_dict[freq]:  # 抽出来后，这摞书是空的
            del self.freq_to_dict[freq]  # 移除空字典
            if self.min_freq == freq:  # 这摞书是最左边的
                self.min_freq += 1
        lst[1] += 1  # 看书次数 +1
        self.freq_to_dict[freq + 1][key] = None
        self.freq_to_dict[freq + 1].move_to_end(key, last=False)  # 放在右边这摞书的最上面
        return lst

    def get(self, key: int) -> int:
        lst = self.get_list(key)
        return lst[0] if lst else -1

    def put(self, key: int, value: int) -> None:
        lst = self.get_list(key)
        if lst:  # 有这本书
            lst[0] = value  # 更新 value
            return
        if len(self.key_to_value_and_freq) == self.capacity:  # 书太多了
            # 移除最左边那摞书的最下面的书
            k, _ = self.freq_to_dict[self.min_freq].popitem()
            del self.key_to_value_and_freq[k]
            if not self.freq_to_dict[self.min_freq]:  # 移除后，这摞书是空的
                del self.freq_to_dict[self.min_freq]  # 移除空字典
        self.key_to_value_and_freq[key] = [value, 1]  # 新书
        self.freq_to_dict[1][key] = None
        self.freq_to_dict[1].move_to_end(key, last=False)  # 放在「看过 1 次」的最上面
        self.min_freq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)