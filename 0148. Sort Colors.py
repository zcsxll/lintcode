class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        left, right = 0, len(nums) - 1
        while left < len(nums) and nums[left] == 0:
            left += 1
        while right >= 0 and nums[right] == 2:
            right -= 1

        i = left + 1
        while left < right and i <= right:
            if nums[i] == 2:
                nums[i] = nums[i] ^ nums[right]
                nums[right] = nums[i] ^ nums[right]
                nums[i] = nums[i] ^ nums[right]
                right -= 1
            elif nums[i] == 0:
                nums[i] = nums[i] ^ nums[left]
                nums[left] = nums[i] ^ nums[left]
                nums[i] = nums[i] ^ nums[left]
                left += 1
            else:
                i += 1

            while left < len(nums) and nums[left] == 0:
                left += 1
            while right >= 0 and nums[right] == 2:
                right -= 1
            if i <= left:
                i = left + 1
            # print(a, left, i, right)

if __name__ == '__main__':
    a = [1, 0, 1, 2, 0, 2]
    a = [2,0,0,1,2,0,2]
    # a = [0,2,2,2,2,1,0,1,0,0,0,1,0,2,0]
    Solution().sortColors(a)
    print(a)