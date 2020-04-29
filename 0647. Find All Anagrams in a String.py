class Solution:
    """
    @param s: a string
    @param p: a string
    @return: a list of index
    """
    def findAnagrams(self, s, p):
        # write your code here
        # bitmap = np.zeros(123)
        bitmap = [0] * 123
        for c in p:
            bitmap[ord(c)] += 1
        # print(bitmap[97:])
        left = 0 #窗左边，闭区间
        right = 0 #窗右边，闭区间
        cnt = 0 #匹配计数
        ret = []
        while right < len(s):
            bitmap[ord(s[right])] -= 1
            if bitmap[ord(s[right])] >= 0: #字符在p中，且引用数量小于等于p中的含量
                cnt += 1
            if right - left + 1 == len(p): #窗长等于p时，左右指针同时滑动，否则只滑动右指针
                if cnt == len(p): #计数长度和p长度一致，则当前窗如何要求
                    # print(left)
                    ret.append(left)
                bitmap[ord(s[left])] += 1 #left即将划过这个字符，因此需要+=1
                if bitmap[ord(s[left])] > 0: #如果这个字符对应的bitmap大于0，说明它是p中的某个字符，而下一刻，这个字符即将不在窗里，因此计数-=1
                    cnt -= 1
                left += 1
            right += 1
            # print(s[right-1], left, right, cnt, bitmap[97:97+5])
        return ret


if __name__ == "__main__":
    s =  "cbaebabacd"
    p = "abc"
    ret = Solution().findAnagrams(s, p)
    print(ret)