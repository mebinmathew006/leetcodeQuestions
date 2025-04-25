class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        di={}
        count=0
        for i in nums:
            if i in di:
                di[i]+=1
            else:
                di[i]=1
        key=dict(sorted(di.items(),key=lambda x: x[1],reverse=True))
        return [x for i,x in enumerate(key.keys()) if i<k ]
            
