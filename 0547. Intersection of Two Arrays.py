class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # write your code here
        ret = set()
        m = {}
        for n in nums2:
            m[n] = 1
        for n in nums1:
            if n in m.keys():
                ret.add(n)
        return list(ret)

if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    ret = Solution().intersection(nums1, nums2)
    print(ret)