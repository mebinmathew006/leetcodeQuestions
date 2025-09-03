class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps={'}':'{',']':'[',')':'('}
        for i in s:
            if i in maps.values():  # opening brackets
                stack.append(i)
            elif i in maps:  # closing brackets
                if not stack or stack[-1] != maps[i]:
                    return False   # mismatch or empty stack
                stack.pop()

        return len(stack)==0
                
            