class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        numbers.sort()
        # print(numbers)
        rets = []
        for idx, n in enumerate(numbers):
            if idx > 0 and n == numbers[idx - 1]:
                # print("skip", idx, n)
                continue
            left, right = idx + 1, len(numbers) - 1
            target = -n
            while left < right:
                if numbers[left] + numbers[right] == target:
                    # print(n, numbers[left], numbers[right])
                    rets.append([n, numbers[left], numbers[right]])
                    left += 1
                    right -= 1
                    while left < right and numbers[left] == numbers[left - 1]:
                        left += 1
                    while left < right and numbers[right] == numbers[right + 1]:
                        right -= 1
                elif numbers[left] + numbers[right] > target:
                    right -= 1
                else:
                    left += 1
        return rets

if __name__ == "__main__":
    import numpy as np
    numbers = np.array([-1,0,1,2,-1,-4])
    numbers = np.array([1,0,-1,-1,-1,-1,0,1,1,1])
    ret = Solution().threeSum(numbers)
    print(ret)