
class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        output = []
        if n == 1:
            output.append("1")
            return output
        for i in range(1, len(n + 1)):
                if i % 3 == 0:
                    output.append("Fizz")
                if i % 5 == 0:
                    output.append("Buzz")
                if i % 3 == 0 and i % 5 == 0:
                    output.append("FizzBuzz")
                else:
                    output.append("{i}")
        return output

if __name__ == "__main__":
    solution = Solution()
    n = 3
    output = solution.fizzBuzz(n)
    print(output)