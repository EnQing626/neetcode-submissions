class FreqStack:

    def __init__(self):
        self.stacks = []  # 栈套栈，stacks 中的每个元素都是一个栈
        self.cnt = defaultdict(int)  # 每个 val 的出现次数

    def push(self, val: int) -> None:
        if self.cnt[val] == len(self.stacks):  # 这个元素的频率已经是目前最多的，现在又出现了一次
            self.stacks.append([val])  # 那么必须创建一个新栈
        else:
            self.stacks[self.cnt[val]].append(val)  # 否则就压入对应的栈
        self.cnt[val] += 1  # 更新频率

    def pop(self) -> int:
        val = self.stacks[-1].pop()  # 弹出最右侧栈的栈顶元素
        if not self.stacks[-1]:  # 弹出后，最右侧栈为空
            self.stacks.pop()  # 删除
        self.cnt[val] -= 1  # 更新频率
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()