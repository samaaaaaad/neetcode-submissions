class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        unique_nums = set()
        for i in range(len(nums)):
            unique_nums.add(nums[i])
        num = len(unique_nums) + 1
        for i in range(num):
            if i not in unique_nums:
                return i
        