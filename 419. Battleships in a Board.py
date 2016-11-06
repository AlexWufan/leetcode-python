class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        for x in board:
        	if x.count('X') > count:
        		count = x.count('X')
        return count