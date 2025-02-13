class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictss={}
        for i in nums:
            if i in dictss.keys():
                dictss[i]+=1
            else:
                dictss[i]=1

            if dictss[i]>len(nums)/2:
                return i

            

            