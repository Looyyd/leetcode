class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums) - 1

        while 1:
            middle = (right + left )/2

            value_middle = nums[middle]

            if value_middle == target:
                return middle

            # exchausted search:
            if middle == left:
                # if right = left + 1, right could be the target
                if nums[right] == target:
                    return right
                else:
                    return -1

            if value_middle < target:
                left = middle
            else:
                right = middle
