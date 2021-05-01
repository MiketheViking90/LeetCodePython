from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        row_members = {}
        col_members = {}
        cell_members = {}

        for i in range(n+1):
            row_members[i] = set()
            col_members[i] = set()
            cell_members[i] = set()

        for row in range(n):
            for col in range(n):
                val_str = board[row][col]
                if val_str == '.':
                    continue

                val = int(val_str)
                cell_no = int((row//3) + 3*(col//3))
                if val in row_members[row]:
                    return False
                row_members[row].add(val)

                if val in col_members[col]:
                    return False
                col_members[col].add(val)

                if val in cell_members[cell_no]:
                    return False
                cell_members[cell_no].add(val)
        return True
