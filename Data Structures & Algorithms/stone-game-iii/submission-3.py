class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            currSum = 0
            maxDiff = float('-inf')
            minEnd, maxEnd = i, min(i + 2, n - 1)
            for j in range(minEnd, maxEnd + 1):
                currSum += stoneValue[j]
                maxDiff = max(maxDiff, currSum - dp[j + 1])
            dp[i] = maxDiff
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"