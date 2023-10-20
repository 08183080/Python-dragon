class Solution:
    
    # chatgpt可以
    def tupleSameProduct(self, nums: list[int]) -> int:
        from collections import defaultdict  # 常规的dict不能access和modify keys that don’t exist in the dictionary. 
        map = defaultdict(int)
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                v = nums[i] * nums[j]
                map[v] +=1
                ans += (map[v]-1) * 8
                print(ans)
        return ans
    
if __name__ == "__main__":
    s = Solution()
    nums = [2,3,4,6]
    ans = s.tupleSameProduct(nums=nums)
    print(ans)
