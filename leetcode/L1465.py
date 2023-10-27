class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: list[int], verticalCuts: list[int]) -> int:
        """
        绝对暴力, 无脑惨胜
        """
        mod = 1000000007
        horizontalCuts.sort()
        verticalCuts.sort()
        hh = []
        vv = []
        hn = len(horizontalCuts)
        vn = len(verticalCuts)
        hh.append(horizontalCuts[0])
        for i in range(1, hn):
            hh.append(horizontalCuts[i] - horizontalCuts[i - 1])
        hh.append(h - horizontalCuts[hn - 1])        
        print(hh)


        vv.append(verticalCuts[0])
        for i in range(1, vn):
            vv.append(verticalCuts[i] - verticalCuts[ i - 1])
        vv.append(w - verticalCuts[vn - 1])
        print(vv)

        # ans = 0
        amax = max(hh)
        bmax = max(vv)
        print(amax)
        print(bmax) 
        ans = 0
        ans = int((amax * bmax) % mod)  # 太大的数太大的数 int()
        return ans
    
if __name__ == "__main__":
    h = 1000000000
    w = 1000000000
    horizontalCuts = [2]
    verticalCuts = [2]
    s = Solution()
    ans = s.maxArea(h, w, horizontalCuts, verticalCuts)  # 预期结果 81
    print(ans)