from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {}
        def inbounds(a, b):
            return 0 <= a < len(matrix) and 0 <= b < len(matrix[0])
        def longest_path_from(i,j):
            key = (i,j)
            if key in cache:
                return cache[key]
            else:
                directions = [
                    (0,1),
                    (0,-1),
                    (1,0),
                    (-1,0)
                ]
                path_len = 1
                for direction in directions:
                    coord = tuple(a + b for a, b in zip(direction,key))
                    if inbounds(*coord) and matrix[coord[0]][coord[1]] > matrix[i][j]:
                        path_len = max(path_len, 1 + longest_path_from(*coord))
                cache[key] = path_len
                return path_len
        ans = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, longest_path_from(i,j))
        return ans


    def longestIncreasingPath2(self, matrix: List[List[int]]) -> int:
        #dp solution
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = [[1] * cols for _ in range(rows)]

        # Flatten the matrix into a list of coordinates sorted by their values
        coords = [(i, j) for i in range(rows) for j in range(cols)]
        coords.sort(key=lambda x: matrix[x[0]][x[1]])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        ans = 1
        for x, y in coords:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] < matrix[x][y]:
                    dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)

            ans = max(ans, dp[x][y])

        return ans
