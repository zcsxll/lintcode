class Solution:
    """
    @param nums: a integer array
    @return: nothing
    """
    def reverseArray(self, nums):
        # write your code here
        left = 0
        right = len(nums) - 1
        while left < right:
            nums[left] = nums[left] ^ nums[right]
            nums[right] = nums[left] ^ nums[right]
            nums[left] = nums[left] ^ nums[right]
            left += 1
            right -= 1

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    Solution().reverseArray(nums)
    print(nums)