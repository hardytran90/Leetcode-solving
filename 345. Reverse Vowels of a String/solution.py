'''
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        # in Python strings are immutable -> converts string into list  
        input_list = list(s)
        left = 0
        right = len(input_list) - 1
        vowels = {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"}
        while left < right:
            if input_list[left] not in vowels:
                left += 1
                continue
            else:
                if input_list[right] not in vowels:
                    right -= 1
                    continue
                else:
                    input_list[left], input_list[right] = input_list[right], input_list[left]
                    left += 1
                    right -= 1
        result = "".join(input_list)
        return result

if __name__ == "__main__":
    solution = Solution()
    s = "leetcode"
    arr = solution.reverseVowels(s)
    print(arr)