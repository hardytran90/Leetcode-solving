'''You are given an array of strings words and a string chars.
A string is good if it can be formed by characters from chars 
(each character can only be used once for each word in words).

Return the sum of lengths of all good strings in words.

Example 1:
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 
Constraints:
1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
words[i] and chars consist of lowercase English letters.'''

from collections import Counter
class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        char_count = Counter(chars)
        result = 0
        
        for word in words:
            word_count = Counter(word)
            valid = True
            for ch in word_count:
                if word_count[ch] > char_count[ch]:         # It number of character in word is bigger than number of character in chars, that word is incorrect!
                    valid = False
                    break
            if valid:
                result += len(word)
        return result    
        
if __name__ == "__main__":
    solution = Solution()
    words = ["cat","bt","hat","tree"]
    chars = "atach"
    print(solution.countCharacters(words,chars))