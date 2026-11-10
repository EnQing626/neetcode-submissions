class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def upone(s,i) -> str:
            # 上拨s的第i位数字
            l = list(s)
            if l[i] == '9':
                l[i] = '0'
            else:
                l[i] = str(int(l[i])+1)
            return ''.join(l)

        def downone(s,i) -> str:
            # 下拨s的第i位数字
            l = list(s)
            if l[i] == '0':
                l[i] = '9'
            else:
                l[i] = str(int(l[i])-1)
            return ''.join(l)
        
        def bfs(deadends,target) -> int:
            # 如果target是'0000'则不需要拨动 返回0
            if target == '0000':
                return 0
            
            step = 0 # 拨动次数 初始时没拨所以次数为0
            q = collections.deque()
            visited = set() # 存放已经比较过的字符组合、死亡数字组合 避免死循环
            visited.update(deadends) # 初始化为死亡数字组合

            q.append('0000')
            
            while q:
                length = len(q) # 按层处理队列中的字符串
                for i in range(length):
                    cur = q.popleft() # 当前处理的节点
                    if cur in visited: # 当前节点已经处理过或属于死亡数字组合 所以跳过
                        continue
                    else:
                        visited.add(cur) # 首次比较 加入已经处理的集合
                    # 判断是否满足终止条件
                    if cur == target:
                        return step
                    # 不满足终止条件将所有相邻的节点加入队列
                    for j in range(4): # cur的每位数都可以上拨或下拨 这些都是cur的相邻节点
                        up = upone(cur,j)
                        # 需要判断上拨、下拨后的组合是否合法（在不在visited里） 不合法就跳过
                        if up not in visited:
                            q.append(up)
                        down = downone(cur,j)
                        if down not in visited:
                            q.append(down)
                # 每循环一遍是一次拨动 次数要+1
                step += 1
            # 所有可能都穷举后无法达到target说明不能解锁 返回-1
            return -1
        
        return bfs(deadends,target)