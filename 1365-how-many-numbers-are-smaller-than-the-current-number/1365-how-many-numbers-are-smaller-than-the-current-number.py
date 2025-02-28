class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        hashs=[]
        for i,v in enumerate(nums):
            count=0
            for j,v2 in enumerate(nums):
                if i==j:
                    continue
                elif(v2<v):
                    count+=1
            hashs.append(count)

        return hashs