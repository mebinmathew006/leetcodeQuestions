class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        great=max(candies)
        out=[]
        for i in candies:
            if i+extraCandies>=great:
                out.append(True)
            else:
                out.append(False)

        return out