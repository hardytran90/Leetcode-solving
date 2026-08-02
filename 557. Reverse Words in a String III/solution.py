'''
Given a string s, reverse the order of characters in each word 
within a sentence while still preserving whitespace and initial word order.
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        reversed_words = [word[::-1] for word in words]
        result = ' '.join(reversed_words)
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseWords("Let's take LeetCode contest")) # Output: "s'teL ekat edoCteeL tsetnoc"
    print(solution.reverseWords("Mr Ding")) # Output: "doG gniD"
    