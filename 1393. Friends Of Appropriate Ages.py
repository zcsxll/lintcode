# import numpy as np

class Solution:
    """
    @param ages: 
    @return: nothing
    """
    def numFriendRequests(self, ages):
        # d = np.zeros(121)   
        d = {}
        for age in ages:
            if age not in d.keys():
                d[age] = 1
            else:
                d[age] += 1
        ret = 0
        for age in d.keys():
            for age2 in d.keys():
                if self.ok(age, age2):
                    if age == age2:
                        ret += (d[age] * (d[age] - 1))
                    else:
                        ret += (d[age] * d[age2])
        return int(ret)

    def ok(self, a, b):
        if b <= int(a * 0.5 + 7):
            return False
        if b > a:
            return False
        return True

if __name__ == '__main__':
    ages = [16,17,18]
    # ages = [20,30,100,110,120]
    # ages = [16, 16]
    ret = Solution().numFriendRequests(ages)
    print(ret)