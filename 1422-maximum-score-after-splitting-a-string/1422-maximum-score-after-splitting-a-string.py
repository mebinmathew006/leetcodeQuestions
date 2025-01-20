class Solution:
    def maxScore(self, s: str) -> int:
        count=0
        for i in range(1,len(s)):
            counts=0
            counts=s[:i].count('0')+s[i:].count('1')
            if counts>count:
                count=counts
        return count
        