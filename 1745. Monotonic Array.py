class Solution:
    """
    @param A: a array
    @return: is it monotonous
    """
    def isMonotonic(self, A):
        # Write your code here.
        if len(A) <= 1:
            return True

        flag = 0
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                if flag == 1:
                    return False
                flag = 2
            elif A[i] < A[i-1]:
                if flag == 2:
                    return False
                flag = 1
        return True

if __name__ == '__main__':
    A = [0, 0, 1, 1, 2, 3]
    ret = Solution().isMonotonic(A)
    print(ret)