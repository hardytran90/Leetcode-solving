'''
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        for i, num in enumerate(nums):
            result ^= i ^ num
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.missingNumber([3, 0, 1]))  # Output: 2
    print(solution.missingNumber([0, 1]))     # Output: 2
    print(solution.missingNumber([9,6,4,2,3,5,7,0,1]))  # Output: 8
    print(solution.missingNumber([0]))         # Output: 1