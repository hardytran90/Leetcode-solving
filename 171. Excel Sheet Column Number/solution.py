class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            digit = ord(char) - ord('A') + 1  # A=1, B=2, ..., Z=26
            result = result * 26 + digit
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.titleToNumber("A"))   # Output: 1
    print(solution.titleToNumber("AB"))  # Output: 28
    print(solution.titleToNumber("ZY"))  # Output: 701
    print(solution.titleToNumber("AAA")) # Output: 703