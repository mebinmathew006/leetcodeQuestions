class Solution:
    def largestGoodInteger(self, num: str) -> str:
        li=[f'{i}{i}{i}' for i in range(9,-1,-1)]
        for i in li :
            if i in num:
                return i

        return ""