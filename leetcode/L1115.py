class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """
        dp[i][j]表示第i次投掷骰子, 得到总和为j的方式数
        【边界条件】dp[1][j] = 1, j >= 1 and j <= k 
        【递推方程式】dp[i][j] = sum(dp[i-1][j-x] for x in range(1, k+1) if j-x>=0) 
        """
        mod = 1000000007
        dp = [[0] * (target + 1) for _ in range(n + 1)]

        # 初始化
        for j in range(1, min(k, target) + 1):
            dp[1][j] = 1
        
        for i in range(2, n + 1):
            for j in range(1, target + 1):
                for x in range(1, k + 1):
                    if j - x >= 0:
                        dp[i][j] = (dp[i][j] + dp[i-1][j-x]) % mod

        return dp[n][target]

if __name__ == "__main__":
    s = Solution()
    ans = s.numRollsToTarget(1, 6, 3)
    print(ans)