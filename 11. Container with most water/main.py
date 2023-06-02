class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height) - 1

        maxArea = 0
        while 1:
            right_height = height[right]
            left_height = height[left]
            distance = right - left
            area = min(right_height, left_height) * (distance)
            if area > maxArea:
                maxArea = area

            if distance == 1:
                return maxArea
            else:
                if right_height<left_height:
                    right -= 1
                else:
                    left += 1

