class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if len(matrix) <= 0 or len(matrix[0]) <= 0:
            return 0
        r = 0
        c = len(matrix[0]) - 1
        cnt = 0
        while True:
            # print(r, c)
            if r >= len(matrix) or c < 0:
                break
            if matrix[r][c] == target:
                cnt += 1
                r += 1
            elif matrix[r][c] < target:
                r += 1
            elif matrix[r][c] > target:
                c -= 1
        return cnt

if __name__ == '__main__':
    matrix = [
        [1, 3, 5, 7],
        [2, 4, 7, 8],
        [3, 5, 9, 10]
        ]
    matrix = [[5]]
    matrix = [
        [1,2,3,9],
        [2,3,9,10],
        [9,100,109,200]
        ]
    target = 9
    ret = Solution().searchMatrix(matrix, target)
    print(ret)