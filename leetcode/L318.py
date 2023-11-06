from functools import reduce
from itertools import product

class Solution:
    # def judge(self, s1: str, s2: str) -> bool:
    #     n1, n2 = len(s1), len(s2)
    #     for i in range(n1):
    #         for j in range(n2):
    #             if s1[i] == s2[j]:
    #                 return False
    #     return True
    

    # def maxProduct(self, words: list[str]) -> int:
    #     """
    #     时间复杂度太高。。。
    #     """
    #     n = len(words)
    #     ans = 0
    #     for i in range(n):
    #         for j in range(i, n):
    #             if self.judge(words[i], words[j]):
    #                 ans = max(ans, len(words[i]) * len(words[j]))
    #     return ans

    def maxProduct(self, words: list[str]) -> int:
        masks = [reduce(lambda a, b: a | (1 << (ord(b) - ord('a'))), word, 0) for word in words]
        return max((len(x[1]) * len(y[1]) for x, y in product(zip(masks, words), repeat=2) if x[0] & y[0] == 0), default=0)



if __name__ == "__main__":
    s = Solution()
    words = ["a","aa","aaa","aaaa"]
    ans = s.maxProduct(words)
    print(ans)
