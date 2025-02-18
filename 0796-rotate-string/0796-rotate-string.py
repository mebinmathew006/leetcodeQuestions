class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        for i in range(len(s)):
            goal =goal[-1]+goal[:-1]
            if s==goal:
                return True
        return False