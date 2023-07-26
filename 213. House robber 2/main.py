from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:

        gains = [(0,0)]* len(nums)
        gains_pass_first = [(0,0)]* len(nums)

        gains[0] = (0,nums[0])
        gains_pass_first[0] = (0,0)

        for i in range(1, len(nums)):
            # without option to take first
            previous_gain_pass_first_pass = gains_pass_first[i-1][0]
            previous_gain_pass_first_take = gains_pass_first[i-1][1]
            gain_pass_first_take = nums[i] + previous_gain_pass_first_pass
            gain_pass_first_pass = 0 + max(previous_gain_pass_first_pass, previous_gain_pass_first_take)
            gains_pass_first[i] = (gain_pass_first_pass, gain_pass_first_take)

            # option to take first
            previous_gain_pass = gains[i-1][0]
            previous_gain_take = gains[i-1][1]

            if i == (len(nums) - 1):
                gain_take = 0
            else:
                gain_take = nums[i] + previous_gain_pass
            gain_pass = 0 + max(previous_gain_pass, previous_gain_take)
            gains[i] = (gain_pass, gain_take)

        return max(gains[-1][0], gains[-1][1], gains_pass_first[-1][0], gains_pass_first[-1][1])


