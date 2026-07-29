class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(n - int(str(n)[::-1]))
    
sol = Solution()

print(sol.mirrorDistance(21))  # Output: 9
print(sol.mirrorDistance(1234))  # Output: 3087