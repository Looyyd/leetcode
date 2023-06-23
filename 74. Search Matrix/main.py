class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = n*m - 1

        while 1:
            middle = (right + left )/2

            row , col = middle//m , middle%n
            value_middle = matrix[row][col]

            if value_middle == target:
                return True

            # exchausted search:
            if middle == left:
                # if right = left + 1, right could be the target
                row, col = right// m, right% n
                if matrix[row][col] == target:
                    return True
                else:
                    return False

            if value_middle < target:
                left = middle
            else:
                right = middle