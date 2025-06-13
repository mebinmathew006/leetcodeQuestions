class Solution:
    def isBalanced(self, num: str) -> bool:
        odd=0
        even=0
        for index,value in enumerate(num):
            if index%2==0:
                even+=int(value)
            else:
                odd +=int(value)

        if odd==even:
            return True

        return False
