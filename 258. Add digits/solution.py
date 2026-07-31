'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
'''
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.addDigits(38))  # Output: 2
    print(solution.addDigits(0))   # Output: 0
    print(solution.addDigits(12345))  # Output: 6