
class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        output = []
        if n == 1:
            output.append("1")
            return output
        else: 
            for i in range(1, n + 1):
                    if i % 3 == 0:
                        if i % 5 == 0:
                            output.append("FizzBuzz")
                        else:
                            output.append("Fizz")
                    elif i % 5 == 0:
                        output.append("Buzz")
                    else:
                        output.append(str(i))
            return output

if __name__ == "__main__":
    solution = Solution()
    n = 15
    output = solution.fizzBuzz(n)
    print(output)