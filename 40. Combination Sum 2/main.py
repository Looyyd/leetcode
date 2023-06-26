from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        self.solutions = []
        candidates.sort()
        def backtrack(remaining_candidates, previous_combination):

            unique_candidates = set()
            for i,candidate in enumerate(remaining_candidates):
                if candidate in unique_candidates:
                    continue
                unique_candidates.add(candidate)
                sum_with_candidate = sum(previous_combination) + candidate
                if sum_with_candidate == target:
                    self.solutions.append([*previous_combination, candidate])
                elif sum_with_candidate < target:
                    next_candidates = remaining_candidates[i+1:]
                    backtrack(next_candidates, [*previous_combination, candidate])

        backtrack(candidates, [])
        return self.solutions


candidates = [2,5,2,1,2]
s= Solution()
print(s.combinationSum2(candidates, 5))