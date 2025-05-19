class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
    
        
        nums1=set(nums1)
        nums2=set(nums2)
        if len(nums1)>len(nums2):
            for i in nums1:
                if i in nums2:
                    return i

        else:
            for i in nums2:
                if i in nums1:
                    return i
                    
        return -1

