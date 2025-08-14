class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        di={}

        for i in nums:
            di[i]=di.get(i,0)+1

        sorted_items = sorted(di.items(),key= lambda x :x[1],reverse = True)

        result = [x[0] for x in sorted_items[:k]]
        return result