class Solution:
    
    def pickGifts(self, gifts: list[int], k: int) -> int:
        """
        周六了, 宿舍浅浅码一下, 同时自我反省。。
        我不要去抱怨, 而要去反省。
        我就是太傲了, 反观自省, 缺乏同理心, 老是觉得别人亏欠自己的, 我太幼稚了。。。
        """
        import heapq
        import math
        q = [-i for i in gifts] # python默认是最小堆, 负数形式表示最大堆...
        heapq.heapify(q) 
        while k > 0:
            x = heapq.heappop(q)
            heapq.heappush(q, -int(math.sqrt(-x)))
            k -= 1
        return -sum(q)

if __name__ == "__main__":
    s = Solution()
    gifts = [25,64,9,4,100]
    k = 4
    print(s.pickGifts(gifts, k))