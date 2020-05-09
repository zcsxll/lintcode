class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        # write your code here
        mask = [[0 for i in range(len(board[0]))] for j in range(len(board))]
        # print(mask)
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == word[0]:
                    mask[y][x] = 1
                    ret = self.zcs(mask, board, word, 1, x, y)
                    if ret is True:
                        return True
                    mask[y][x] = 0
        return False

    def zcs(self, mask, board, word, index, x, y):
        if index == len(word):
            return True
        if x > 0 and board[y][x-1] == word[index] and mask[y][x-1] == 0:
            mask[y][x-1] = 1
            if self.zcs(mask, board, word, index + 1, x - 1, y) is True:
                return True
            mask[y][x-1] = 0
        if y > 0 and board[y-1][x] == word[index] and mask[y-1][x] == 0:
            mask[y-1][x] = 1
            if self.zcs(mask, board, word, index + 1, x, y-1) is True:
                return True
            mask[y-1][x] = 0
        if x < len(board[0]) - 1 and board[y][x+1] == word[index] and mask[y][x+1] == 0:
            mask[y][x+1] = 1
            if self.zcs(mask, board, word, index + 1, x + 1, y) is True:
                return True
            mask[y][x+1] = 0
        if y < len(board) - 1 and board[y+1][x] == word[index] and mask[y+1][x] == 0:
            mask[y+1][x] = 1
            if self.zcs(mask, board, word, index + 1, x, y + 1) is True:
                return True
            mask[y+1][x] = 0
        return False
        

if __name__ == "__main__":
    board = ["ABCE", "SFCS", "ADEE"]
    board = ["ABCE","SFCS","ADEE"]
    word = "ABCCCD"
    word = "ABCB"
    ret = Solution().exist(board, word)
    print(ret)