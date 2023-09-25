from  typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        num_count = {0: 1}  # Initialize with zero sum having 1 way

        for num in nums:
            new_num_count = {}
            for current_sum in num_count:
                new_num_count[current_sum + num] = new_num_count.get(current_sum + num, 0) + num_count[current_sum]
                new_num_count[current_sum - num] = new_num_count.get(current_sum - num, 0) + num_count[current_sum]

            num_count = new_num_count  # Update the count dictionary

        return num_count.get(target, 0)  # Return the number of ways for the target sum, or 0 if not possible




