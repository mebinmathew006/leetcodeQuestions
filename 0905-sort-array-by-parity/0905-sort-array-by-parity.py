class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evenindex=0
        oddindex=-1
        result=[0]*len(nums)
        for i in nums:
            if i%2==0:
                result[evenindex]=i
                evenindex+=1
            else:
                result[oddindex]=i
                oddindex-=1

        return result