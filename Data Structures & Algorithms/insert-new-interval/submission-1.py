class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans=[]
        for i in range(len(intervals)):
            if intervals[i][0]>newInterval[1]:
                ans.append(newInterval)
                return ans+intervals[i:]
            elif newInterval[0]>intervals[i][1]:
                ans.append(intervals[i])
            else:
                newInterval=[min(intervals[i][0],newInterval[0]),max(intervals[i][1],newInterval[1])]
        ans.append(newInterval)
        return ans