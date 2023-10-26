class Solution:
    def countDigits(self, num: int) -> int:
        ans = 0
        n = num
        while num > 0:
            a = num % 10
            if n % a == 0:
                # print(a)
                ans += 1
            num = num // 10  # // 才是整除
            # print(num)
        return ans 