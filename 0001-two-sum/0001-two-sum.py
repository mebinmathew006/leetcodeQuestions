class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicts={}
        for i,j in enumerate(nums):
            if target-j in dicts:
                return i,dicts[target-j]
            else:
                dicts[j]=i
            