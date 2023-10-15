from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        inv_ans = []

        for i in range(len(temperatures)-1,-1, -1):
            temp = temperatures[i]
            while stack and stack[-1][0] <= temp:
                stack.pop()
            inv_ans.append(stack[-1][1]-i if stack else 0)
            stack.append((temp, i))

        inv_ans.reverse()
        return inv_ans

class Solution2:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # Stack to store indices of temperatures.
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index

            stack.append(i)

        return result