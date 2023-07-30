from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) -1

        while 1:
            middle = (left + right)//2
            right_val = nums[right]
            left_val = nums[left]
            middle_val = nums[middle]

            if right == (left+1) and right_val<left_val:
                return right_val


            # check if a segment goes from bigger to smaller, then min is there
            if (middle_val<left_val):
                right=middle
            elif (right_val<middle_val):
                left=middle
            # if only goes up then the first element is the min
            else:
                return left_val

