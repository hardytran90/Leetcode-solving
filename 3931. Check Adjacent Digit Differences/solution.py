'''
You are given a string s consisting of digits.
Return true if the absolute difference between every pair of adjacent digits is at most 2, 
otherwise return false.
The absolute difference between a and b is defined as abs(a - b).

Example 1:
Input: s = "132"
Output: true

Explanation:
The absolute difference between digits at s[0] and s[1] is abs(1 - 3) = 2.
The absolute difference between digits at s[1] and s[2] is abs(3 - 2) = 1.
Since both differences are at most 2, the answer is true.

Example 2:
Input: s = "129"
Output: false

Explanation:
The absolute difference between digits at s[0] and s[1] is abs(1 - 2) = 1.
The absolute difference between digits at s[1] and s[2] is abs(2 - 9) = 7, which is greater than 2.
Therefore, the answer is false.
 
Constraints:
2 <= s.length <= 100
s consists only of digits.
'''

class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        for ch in range(0, len(s) - 1):
            if abs(int(s[ch]) - int(s[ch + 1])) > 2:
                return False
        return True

if __name__ == "__main__":
    solution = Solution()
    s = "129"
    print(solution.isAdjacentDiffAtMostTwo(s))