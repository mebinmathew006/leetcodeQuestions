class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # return [x for x in range(1,len(nums)+1) if x not in set(nums)]

        ret=[]
        set_nums=set(nums)
        for i in range(1,len(nums)+1):
            if i not in set_nums:
                ret.append(i)

        return ret
