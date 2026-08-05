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
        print(char_to_row)
        
if __name__ == "__main__":
    solution = Solution()
    words = ["Hello","Alaska","Dad","Peace"]
    solution.findWords(words)