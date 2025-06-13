class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dicts={}

        for i in arr:
            if i in dicts:
                dicts[i]=dicts[i]+1
            else:
                dicts[i]=1
        
        if len(set(dicts.values()))==len(dicts):
            return True

        return False