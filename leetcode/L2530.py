import heapq
class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        q = [-x for x in nums]  # heapq默认是小根堆...
        heapq.heapify(q)

        ans = 0
        for _ in range(k):
            x = heapq.heappop(q)
            ans += -x
            heapq.heappush(q, -((-x+2)//3))
        return ans    

if __name__ == "__main__":
    s = Solution()
    nums = [1,10,3,3,3]
    k = 3
    ans = s.maxKelements(nums=nums, k=k)
    print(ans)