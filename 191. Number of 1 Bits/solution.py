'''
Given a positive integer n, write a function that returns the number of set bits 
in its binary representation (also known as the Hamming weight).
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1 
            n >>= 1           
        return count

if __name__ == "__main__":
    solution = Solution()
    print(solution.hammingWeight(11))  # Output: 3 (binary representation: 1011)
    print(solution.hammingWeight(128)) # Output: 1 (binary representation: 10000000)