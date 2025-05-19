class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        lage=float('-inf')
        nums=set(nums)
        for i in nums:
            if (0-i) in nums and i >0:
                if lage < i:
                    lage =i
        if lage !=float('-inf'):
            return lage

        return -1
        