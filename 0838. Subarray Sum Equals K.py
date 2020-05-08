class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the number of continuous subarrays whose sum equals to k
    """
    def subarraySumEqualsK(self, nums, k):
        # write your code here
        sum = [0] + nums[:]
        for i in range(1, len(sum)): #计算前缀和
            sum[i] += sum[i - 1]
        # print(sum)
        zcs = dict()
        cnt = 0
        for s in sum:
            if (s - k) in zcs.keys(): #如果当前s是[0,6]的和，s-k存在且是[0,3]的和，则说明存在一个和为k的连续区间[4,6]
                cnt += zcs[s - k] #如果[0,4]的和也是s-k，则zcs[s-k] = 2，那么[5,6]也符合要求
            if s in zcs.keys(): #上边两行用到的s-k就是在这里记录的
                zcs[s] += 1
            else:
                zcs[s] = 1
        return cnt

if __name__ == "__main__":
    nums = [1,1,1]
    k = 2
    nums = [-10,3,2,-6,-6,0,0,0,-7,15,-5,5,-8,-3,-5,1,-2,-2,8,-8,6]
    k = 15
    ret = Solution().subarraySumEqualsK(nums, k)
    print(ret)