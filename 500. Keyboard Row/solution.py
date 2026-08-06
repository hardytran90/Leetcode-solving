'''
Given an array of strings words, return the words that can be typed 
using letters of the alphabet on only one row of American keyboard like the image below.

Note that the strings are case-insensitive, 
both lowercased and uppercased of the same letter are treated as if they are at the same row.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".
'''

'''
Example 1:
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Explanation:
Both "a" and "A" are in the 2nd row of the American keyboard due to case insensitivity.

Example 2:
Input: words = ["omk"]
Output: []

Example 3:
Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]
'''

class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        char_to_row = {}
        for i, row in enumerate(rows):
            for ch in row:
                char_to_row[ch] = i
    # char_to_row format: {'q': 0, 'w': 0, 'e': 0, 'a': 1, 's': 1, 'z': 2, 'x': 2, ...}
    
    def is_valid(word, char_to_row):
        lower_word = word.lower()
        first_row = char_to_row[lower_word[0]]
        
        for ch in lower_word:
            if char_to_row[ch] != first_row:
                return False
            return True
        
if __name__ == "__main__":
    solution = Solution()
    words = ["Hello","Alaska","Dad","Peace"]
    solution.findWords(words)