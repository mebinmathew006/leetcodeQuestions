class Solution:
    def trimMean(self, arr: List[int]) -> float:
        last_five=int((5/100)*len(arr)) 
        arr.sort()      
        return sum(arr[last_five:-last_five])/len(arr[last_five:-last_five])
        