class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited =set()
        left=right=0
        max_length = 0
        while right<len(s):
            if s[right] not in visited:
                visited.add(s[right])
                right+=1
                max_length= max(max_length,right-left)
            else:
                visited.remove(s[left])
                left+=1

        return max_length




