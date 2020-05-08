class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        # write your code here
        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                cc = stack.pop()
                if c == ')' and cc != '(':
                    return False
                if c == ']' and cc != '[':
                    return False
                if c == '}' and cc != '{':
                    return False
        return len(stack) == 0

if __name__ == "__main__":
    s = '()[]{}}'
    ret = Solution().isValidParentheses(s)
    print(ret)