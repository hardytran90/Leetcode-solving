'''
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent. 
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons). 
Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = "2"
Output: ["a","b","c"]
 
Constraints:
1 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        number_map = {'2':["a","b","c"], '3':["d","e","f"], '4':["g","h","i"], '5':["j","k","l"], 
                      '6':["m","n","o"], '7':["p","q","r","s"], '8':["t","u","v"], '9':["w","x","y","z"]}
        
        if digits == "":
            return []
        
        result = []
        
        def backtrack(index, path):
            if index == len(list(digits)):
                result.append(path)
                return
            
            current_digit = digits[index]
            letters = number_map[current_digit]
            
            for let in letters:
                backtrack(index + 1, path + let)
        
        backtrack(0, "")
        return result

if __name__ == "__main__":
    solution = Solution()
    digits = "23"
    print(solution.letterCombinations(digits))
                