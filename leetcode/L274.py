class Solution:
    def hIndex(self, citations: list[int]) -> int:
        """
        h指数 计算器...

        排序 
        """
        citations.sort(reverse=True)  # 降序
        h = 0
        i = 0
        n = len(citations)
        while i < n and citations[i] > h:
            h += 1        
            i += 1 
        return h
    
    def hindex(self, citations: list[int]) -> int:
        return sum(x > i for i, x in enumerate(sorted(citations, reverse = True)))

if __name__ == "__main__":
    s = Solution()
    c = [7, 8, 9]
    ans = 0
    ans = s.hindex(c)
    print(ans)