class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        di={}
        for i in nums:
            if i in di:
                di[i]+=1
            else:
                di[i]=1
        
        return [x for x in di.keys() if di[x] >1]