class Solution:
    """
    @param a: a number
    @param b: a number
    @return: the result
    """
    def addBinary(self, a, b):
        # write your code here
        ia = len(a) - 1
        ib = len(b) - 1
        carry = 0
        out = ''
        while ia >= 0 and ib >= 0:
            na = int(a[ia])
            nb = int(b[ib])
            ret = na + nb + carry
            carry = ret // 2
            ret %= 2
            # print(ret, carry)
            out = str(ret) + out
            ia -= 1
            ib -= 1
        while ia >= 0:
            na = int(a[ia])
            ret = na + carry
            carry = ret // 2
            ret %= 2
            # print(ret)
            out = str(ret) + out
            ia -= 1
        while ib >= 0:
            nb = int(b[ib])
            ret = nb + carry
            carry = ret // 2
            ret %= 2
            # print(ret)
            out = str(ret) + out
            ib -= 1
        if carry == 1:
            # print(carry)
            out = str(carry) + out
        return out

if __name__ == "__main__":
    a = '11'
    b = '1'
    ret = Solution().addBinary(a, b)
    print(ret)