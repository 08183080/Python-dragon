"""
2023/10/22 leetcode daily problem
"""
class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        """
        暴力

        1. sort, 2. dp
        你可以按 任意 顺序安排做菜的顺序，你也可以选择放弃做某些菜来获得更大的总和。
        dp[i] = max(dp[i-1], dp[i-1]+sa[i]*time[i])
        time[i] = time[i-1] + 1?

        how to dp?
        1. formula
        2. initial
        """
        satisfaction = sorted(satisfaction)
        # print(satisfaction)
        n = len(satisfaction)
        ans = 0
        for i in range(n):
            res = 0
            for j in range(i, n):
                res += satisfaction[j] * (j-i+1)
            ans = max(ans, res)
        return ans
    
    def maxSatisfaction2(self, satisfaction: list[int]) -> int:
        """
        greedy
        """
        satisfaction.sort(key = lambda x:-x)    # python lambda sort
        n = len(satisfaction)
        pre, ans = 0, 0
        for si in satisfaction:
            if pre + si > 0:
                pre += si
                ans += pre
            else:
                break
        return ans


if __name__ == "__main__":
    s = Solution()
    satisfaction = [-1,-8,0,5,-9]
    ans = s.maxSatisfaction2(satisfaction)
    print(ans)