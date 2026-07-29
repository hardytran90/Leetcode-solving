class Solution:
    def reverse(self, n: int) -> int:
        res = 0
        while n > 0:
            res = res * 10 + n % 10
            n //= 10
        return res

    def mirrorDistance(self, n: int) -> int:
        return abs(n - self.reverse(n))
    
sol = Solution()
print(sol.mirrorDistance(21))  # Output: 9
print(sol.mirrorDistance(1234))  # Output: 3087