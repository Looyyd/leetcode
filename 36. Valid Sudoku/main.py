class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        line_hashmap = [{} for _ in range(9)]
        column_hashmap = [{} for _ in range(9)]
        square_hashmap = [{} for _ in range(9)]

        for line_index, line in enumerate(board):
            for column_index, number in enumerate(line):
                if number == ".":
                    continue

                if line_hashmap[line_index].get(number):
                    return False
                else:
                    line_hashmap[line_index][number] = True

                if column_hashmap[column_index].get(number):
                    return False
                else:
                    column_hashmap[column_index][number] = True

                square_index = (line_index // 3) * 3 + column_index // 3

                if square_hashmap[square_index].get(number):
                    return False
                else:
                    square_hashmap[square_index][number] = True

        return True



board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

s = Solution()
print(s.isValidSudoku(board))




