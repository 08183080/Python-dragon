class Solution:
    def punishmentNumber(self, n: int) -> int: 
        def find(num: int,s: str, pos: int, sum: int) -> bool:
            """
            判断字符串是否满足存在数据段, 使其数字化之后, 各位之和相加等于初始数据.
            """
            if pos == len(s): # 终止条件
                print(sum, num)
                return sum == num
            cur = 0
            for i in range(pos, len(s)):
                cur = cur * 10 + int(s[i])
                if (sum + cur> num):
                    break
                if find(num, s, i+1, sum + cur): 
                    # print(sum)
                    return True 
            return False    

        ans = 0
        for i in range(1, n+1):
            t = i * i
            if find(i, str(t), 0, 0):
                ans += t
        return ans


if __name__ == "__main__":
    s = Solution()
    n = 10
    print(s.punishmentNumber(n))
