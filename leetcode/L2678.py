class Solution:
    def countSeniors(self, details: list[str]) -> int:
        # ans = 0
        # for detail in details:
        #     if int(detail[11:13]) > 60:
        #         ans += 1
        # return ans
        return sum(1 for detail in details if detail[11:13] > '60')
    
if __name__ == "__main__":
    s = Solution()
    detailes = ["7868190130M7522","5303914400F9211","9273338290F4010"]
    ans = s.countSeniors(detailes)
    print(ans)