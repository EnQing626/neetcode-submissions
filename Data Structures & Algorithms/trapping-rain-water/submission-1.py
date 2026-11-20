class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        stack=[0]
        for i in range(1,len(height)):
            if height[i]<height[i-1]:
                stack.append(i)
            elif height[i]==height[i-1]:
                stack.pop()
                stack.append(i)
            else:
                while stack and height[stack[-1]] < height[i]:
                    right_height=height[i]
                    mid_height=height[stack[-1]]
                    stack.pop()
                    if stack:
                        left_height=height[stack[-1]]
                        h=min(left_height,right_height)-mid_height
                        w=i-stack[-1]-1
                        res+=h*w
                stack.append(i)
        return res