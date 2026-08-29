allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]

class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        result = []

        for word in words:
            valid = True
            for ch in word:
                if ch not in allowed:
                    valid = False
                    break
            if valid:
                result.append(word)
        return len(result)
    
if __name__ == "__main__":
    solution = Solution()
    allowed = "ab"
    words = ["ad","bd","aaab","baa","badab"]
    print(solution.countConsistentStrings(allowed, words))