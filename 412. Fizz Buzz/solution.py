'''
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
'''

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