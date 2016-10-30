class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [[] for _ in range(9)]
        col = [[] for _ in range(9)]
        cell = [[[] for _ in range(3) ] for _ in range(3)]


        for i in range(9):
        	for j in range(9):
        		if board[i][j] != '.':
        			if board[i][j] in row[i]:
        				return False
        			else: row[i].append(board[i][j])
        			if board[i][j] in col[j]:
        				return False
        			else: col[j].append(board[i][j])
        			if board[i][j] in cell[i//3][j//3]:
        				return False
        			else: cell[i//3][j//3].append(board[i][j])
        		else: continue
        return True
