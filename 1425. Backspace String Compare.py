class Solution:
    """
    @param S: string S
    @param T: string T
    @return: Backspace String Compare
    """
    def backspaceCompare(self, S, T):
        # Write your code here
        s1 = ''
        for c in S:
            if c == '#':
                s1 = s1[:-1]
            else:
                s1 += c
        s2 = ''
        for c in T:
            if c == '#':
                s2 = s2[:-1]
            else:
                s2 += c
        # print(s1, s2)
        return s1 == s2

if __name__ == '__main__':
    S = "ab#c"
    T = "ad#c"
    ret = Solution().backspaceCompare(S, T)
    print(ret)