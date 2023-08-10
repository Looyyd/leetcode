from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        curr_capacity = 0

        for i in range(0, len(nums)-1):
            num = nums[i]
            curr_capacity = max(num, curr_capacity-1)
            if curr_capacity == 0:
                return False

        return True




