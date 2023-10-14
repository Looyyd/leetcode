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
