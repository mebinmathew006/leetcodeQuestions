class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if not nums[i] >target:
                for j in range(i+1,len(nums)):
                    if nums[i]+nums[j]==target:
                        return [i,j]