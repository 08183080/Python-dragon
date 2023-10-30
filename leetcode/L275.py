class Solution:
    def hIndex(self, citations: list[int]) -> int:
        """
        binary search
        """
        n = len(citations)
        l, r = 0, n - 1
        while (l < r):
            m = (l + r) // 2
            if citations[m] >= n - m:
                r = m
            else:
                l = m + 1 
        return n - r if citations[r] >= n - r else 0

if __name__ == "__main__":
    s = Solution()
    citations = [0,1,3,5,6]
    ans = s.hIndex(citations)
    print(ans)
