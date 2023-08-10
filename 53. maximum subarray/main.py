from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]

        current_sum = max_sum

        for i in range(1, len(nums)):
            num = nums[i]
            # if negative sum reset
            if current_sum < 0:
                max_sum = max(current_sum, max_sum)
                current_sum = num
            else:
                if num<0:
                    # we could be at maximum
                    max_sum = max(max_sum, current_sum)
                current_sum += num

        max_sum = max(current_sum, max_sum)

        return max_sum
