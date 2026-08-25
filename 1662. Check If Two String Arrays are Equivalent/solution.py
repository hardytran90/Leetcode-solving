'''
Given two string arrays word1 and word2, 
return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

Example 1:
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.

Example 2:
Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false

Example 3:
Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true

Constraints:
1 <= word1.length, word2.length <= 103
1 <= word1[i].length, word2[i].length <= 103
1 <= sum(word1[i].length), sum(word2[i].length) <= 103
word1[i] and word2[i] consist of lowercase letters.
'''

class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        '''
        string1 = ''
        string2 = ''
        for i in range(len(word1)):
            string1 = string1 + word1[i]
        for i in range(len(word2)):
            string2 = string2 + word2[i]
        return string1 != string2
        '''
        
        ''' Shorter solution
         return ''.join(word1) == ''.join(word2) '''
    
        # Two pointers solution
        
        i, j = 0, 0      # each string group's index in an array
        p1, p2 = 0, 0     # each element index in each group
        
        while i < len(word1) and j < len(word2):
            if word1[i][p1] != word2[j][p2]:
                return False
            
            p1 += 1
            p2 += 1
            
            if p1 == len(word1[i]):
                i += 1
                p1 = 0
            if p2 == len(word2[j]):
                j += 1
                p2 = 0

        # Make sure traversal all of elements
        return i == len(word1) and j == len(word2)

if __name__ == "__main__":
    solution = Solution()
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    print(solution.arrayStringsAreEqual(word1, word2))