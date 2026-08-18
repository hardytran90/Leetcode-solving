'''
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. 
The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. 
Do not include any extra spaces.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

Constraints:
1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)
        n = len(chars)

        # Use 2 pointers to clear unnecessary spaces before and after words
        # fast pointer always goes before slow pointer
        slow = 0
        for fast in range(n):
            if chars[fast] != ' ':
                if slow != 0 and chars[fast - 1] == ' ': # At the beginning of next word: slow = ' ', fast = first character of next word => set slow = space, plus 1 slow, set slow = fast <= first character
                    chars[slow] = ' '
                    slow += 1
                chars[slow] = chars[fast]
                slow += 1
        chars = chars[:slow]  # Ignore the left spaces at the end of string
        n = slow

        self.reverse(chars, 0, n - 1)   # Reverse all character positions (All the words are in reversed version)

        # Reverse every single word into right word
        start = 0
        for i in range(n + 1):
            if i == n or chars[i] == ' ':
                self.reverse(chars, start, i - 1)
                start = i + 1

        return ''.join(chars)

    # Helper function
    def reverse(self, arr, left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    
if __name__ == "__main__":
    solution = Solution()
    s1 = "the sky is blue"
    s2 = "  hello world  "
    s3 = "a good   example"
    print(solution.reverseWords(s1))
    print(solution.reverseWords(s2))
    print(solution.reverseWords(s3))