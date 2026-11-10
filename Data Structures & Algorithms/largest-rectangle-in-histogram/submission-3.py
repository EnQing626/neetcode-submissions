class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        heights.insert(0,0)
        heights.append(0)
        stack=[0]
        result=0
        for i in range(1, len(heights)):
            #Condition 1
            if heights[i]>heights[stack[-1]]:
                stack.append(i)
            #Condition 2
            elif heights[i]==heights[stack[-1]]:
                stack.pop()
                stack.append(i)
            else:
                while stack and heights[i]<heights[stack[-1]]:

                    mid_index = stack[-1]
                    stack.pop()
                    if stack:
                        left_index = stack[-1]
                        right_index = i
                        width = right_index-left_index-1
                        height = heights[mid_index]
                        result = max(result, width*height)
                stack.append(i)
        return result
                        
                