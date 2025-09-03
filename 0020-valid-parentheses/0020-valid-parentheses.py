class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps={'}':'{',']':'[',')':'('}
        for i in s:
            if i in maps.values():
                stack.append(i)
            elif i in maps :
                if not stack and  stack[-1]!=maps[i]:
                    return False
                stack.pop(-1)

        return len(stack)==0
                
            