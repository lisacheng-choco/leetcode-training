'''
- Leetcode URL: https://leetcode.com/problems/valid-sudoku/
'''

from typing import List

from importlib_metadata import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def solution1():
            '''
            use 3 Dict[hashset] to determine if the number is duplicated, if it is board[i][j]
            1. rows: Dict, index=i
            2. cols: Dict, index=j
            3. sub: Dict, index=[i//3][j//3]

            - time complexity: O(9^2)
            - space complexity: O(9^2)
            '''
            rows = collections.defaultdict(set)
            cols = collections.defaultdict(set)
            squares = collections.defaultdict(set)

            for i in range(9):
                for j in range(9):
                    num = board[i][j]
                    if num == ".": continue
                    if ((num in rows[i]) or (num in cols[j]) or (num in squares[(i//3, j//3)])):
                        return False
                    rows[i].add(num)
                    cols[j].add(num)
                    squares[((i//3, j//3))].add(num)
      
            return True
            
        return solution1()



input = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
s = Solution()
print(s.isValidSudoku(input))
