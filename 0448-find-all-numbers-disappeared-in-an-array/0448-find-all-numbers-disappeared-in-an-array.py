class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length=len(nums)
        nums=set(nums)
        result=[x for x in range(1,length+1) if x not in nums]
        return result
