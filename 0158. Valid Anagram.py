class Solution:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """
    def anagram(self, s, t):
        # write your code here
        if len(s) != len(t):
            return False
        zcs = [0] * 127
        for a, b in zip(s, t):
            zcs[ord(a)] += 1
            zcs[ord(b)] -= 1
        return True if zcs == [0] * 127 else False

if __name__ == "__main__":
    s = "abc"
    t = "acc"
    ret = Solution().anagram(s, t)
    print(ret)