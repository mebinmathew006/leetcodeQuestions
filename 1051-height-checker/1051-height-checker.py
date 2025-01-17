class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count=0
        expected=heights[:]
        heights.sort()
        for i in range(len(expected)):
            if expected[i]!=heights[i]:
                count+=1
        
        return count
