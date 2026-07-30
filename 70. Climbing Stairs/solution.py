'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Constraints: 1 <= n <= 45
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        step2, step1 = 1, 2
        for i in range(3, n + 1):
            step2, step1 = step1, step2 + step1

        return step1

if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(5))  # Output: 8
    print(solution.climbStairs(6))  # Output: 13