class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count =0
        i=0
        while i < len(nums):
            if nums.count(nums[i])>1:
                val=nums[i]
                count+=1
                nums.remove(val)
                nums.remove(val)
            else:
                i+=1
        return [count,len(nums)]