'''
Given a string s, reverse the string according to the following rules:
All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

Example 1:
Input: s = "ab-cd"
Output: "dc-ba"

Example 2:
Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:
Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

Constraints:
1 <= s.length <= 100
s consists of characters with ASCII values in the range [33, 122].
s does not contain '\"' or '\\'.
'''

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        s = list(s)
        while left < right:
            if s[left].isalpha() == True:
                if s[right].isalpha() == True:
                    s[left], s[right] = s[right], s[left]
                    right -= 1
                    left += 1
                else:
                    right -= 1
            else:
                left += 1
        result = "".join(s)
        return result
    
if __name__ == "__main__":
    solution = Solution()
    s1 = "ab-cd"
    s2 = "a-bC-dEf-ghIj"
    s3 = "Test1ng-Leet=code-Q!"
    print(solution.reverseOnlyLetters(s1))
    print(solution.reverseOnlyLetters(s2))
    print(solution.reverseOnlyLetters(s3))


    