'''
Given two strings ransomNote and magazine, 
return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
'''

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        maga_count = Counter(magazine)
        
        valid = True
        
        for ch in ransom_count:
            if ransom_count[ch] > maga_count[ch]:
                valid = False
                break
        
        return valid
    
if __name__ == "__main__":
    solution = Solution()
    ransomNote = "aa"
    magazine = "aab"
    print(solution.canConstruct(ransomNote, magazine))