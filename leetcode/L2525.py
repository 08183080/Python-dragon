class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        a, b = False, False
        if length >= 1e4 or width >= 1e4 or height >= 1e4 or length*width*height >= 1e9:
            a = True   # "Bulky"
        if mass >= 100:
            b = True    # "Heavy"
        if a and b:
            return "Both"
        elif not a and not b:
            return "Neither"
        elif a and not b:
            return "Bulky"
        else:
            return "Heavy"
    

if __name__ == "__main__":
    s = Solution()
    length = 1000
    width = 35
    height = 700
    mass = 300
    ans = s.categorizeBox(length=length, width=width, height=height, mass=mass)
    print(ans)