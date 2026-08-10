'''
Given a string array words, return an array of all characters 
that show up in all strings within the words (including duplicates). 
You may return the answer in any order.

Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]
'''
from collections import Counter

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        result = Counter(words[0])
        for word in words[1:]:
            result = result & Counter(word)
        return list(result.elements())
            
    
if __name__ == "__main__":
    solution = Solution()
    words = ["bella","label","roller"]
    print(solution.commonChars(words))