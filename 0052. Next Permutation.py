class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        # write your code here
        if len(nums) == 1:
            return nums
        for i in range(len(nums) - 2, -1, -1):
            # print(i)
            if nums[i] < nums[i+1]:#找到转折点i
                break
        else:
            return nums[::-1]

        for j in range(len(nums) - 1, i, -1):#从后往前找到第一个比i打的数字并和i交换
            if nums[j] > nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                break

        # print(index, (len(nums) - index - 1) // 2)
        for j in range((len(nums) - i) // 2):#逆序i之后的数字
            nums[i + j + 1], nums[len(nums) - j - 1] = nums[len(nums) - j - 1], nums[i + j + 1]
            # print(i, len(nums) - 2 - i + index)
        return nums

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    # nums = [4, 3, 2, 1]
    # nums = [1, 2, 3, 2]
    # nums = [1, 3, 0, 13, 12, 11, 10, 9, 8]
    nums = [1, 2]
    # nums = [1, 3, 0, 13, 12, 8]
    nums = Solution().nextPermutation(nums)
    print(nums)