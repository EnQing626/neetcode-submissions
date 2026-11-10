class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:  # 如果数组长度小于 2，直接返回长度
            return n
        
        ans = 1       
        start = 0       # 当前分组的起点索引
        
        for i in range(1, n):
            # 计算 arr[i] 和 arr[i-1] 的比较关系：
            # 如果 arr[i] > arr[i-1]，cmp = 1
            # 如果 arr[i] < arr[i-1]，cmp = -1
            # 如果 arr[i] == arr[i-1]，cmp = 0
            cmp = (arr[i] > arr[i-1]) - (arr[i] < arr[i-1])
            
            if cmp == 0:  
                # 当前元素和前一个相等，turbulence 被打断，重新从当前位置开始新的分组
                start = i
            elif i == n-1 or cmp * ((arr[i+1] > arr[i]) - (arr[i+1] < arr[i])) != -1:
                # 如果到达数组最后一个元素 (i == n-1) 或 当前比较 cmp 和下一次比较的符号不是相反的（说明交替关系被打断）
                # 那么分组到 i 为止结束，计算分组长度
                ans = max(ans, i - start + 1)
                # 下一段分组从当前位置 i 重新开始
                start = i   
        
        return ans