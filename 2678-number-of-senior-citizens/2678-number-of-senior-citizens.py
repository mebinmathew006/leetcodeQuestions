class Solution:
    def countSeniors(self, details: List[str]) -> int:
        counts=0
        for i in details:
            if int(i[-4:-2])>60:
                counts=counts+1
        return counts
