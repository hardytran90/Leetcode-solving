'''
Given n pairs of parentheses, 
write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
 
Constraints:
1 <= n <= 8
'''

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        def backtrack(current, open_count, close_count, n, result):
            if open_count == close_count == n:
                result.append(current)
            
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count, n, result)
                
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1, n, result)
        
        backtrack("", 0, 0, n, result)
        return result
    
if __name__ == "__main__":
    solution = Solution()
    n = 3
    print(solution.generateParenthesis(n))