'''
Given a string text, you want to use the characters of text 
to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. 
Return the maximum number of instances that can be formed.

Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0

Constraints:
1 <= text.length <= 104
text consists of lower case English letters only.
'''

from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word = "balloon"
        word_counter = Counter(word)
        text_counter = Counter(text)
        
        valid = True
        for ch in word_counter:
            if text_counter[ch] < word_counter[ch]:
                valid = False
                nums = 0
                break
            
        if valid:
            nums = []
            for ch in word_counter:
                nums.append(text_counter[ch] // word_counter[ch])
            nums = min(nums)
        
        return nums
    
if __name__ == "__main__":
    solution = Solution()
    text = "loonbalxballpoon"
    print(solution.maxNumberOfBalloons(text))
        