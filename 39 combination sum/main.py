from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        self.solutions = []
        def backtrack(remaining_candidates, current_combination):

            for i,candidate in enumerate(remaining_candidates):
                sum_with_candidate = sum(current_combination) + candidate
                if sum_with_candidate == target:
                    self.solutions.append([*current_combination, candidate])
                elif sum_with_candidate < target:
                    next_candidates = remaining_candidates[i:]
                    backtrack(next_candidates, [*current_combination, candidate])

        backtrack(candidates, [])
        return self.solutions