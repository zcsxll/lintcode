class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        self.ret = []
        # board = ['.' * n] * n
        board = [['.' for i in range(n)] for j in range(n)]
        # print(board)
        self.zcs(board, 0)
        return self.ret

    def zcs(self, board, row):
        if row == len(board):
            # print(board)
            ret = []
            for line in board:
                ret.append(''.join(line))
                # print(line)
            self.ret.append(ret)
            return
        for i in range(len(board)):
            if self.can_place(board, row, i):
                board[row][i] = 'Q'
                self.zcs(board, row + 1)
                board[row][i] = '.'

    def can_place(self, board, row, col):
        for r in range(row):
            if board[r][col] == 'Q':
                return False
            if col > 0 and col - row + r >= 0 and board[r][col - row + r] == 'Q':
                return False
            elif col < len(board) - 1 and col + row - r < len(board) and board[r][col + row - r] == 'Q':
                return False
        return True

if __name__ == '__main__':
    ret = Solution().solveNQueens(1)
    print(ret)