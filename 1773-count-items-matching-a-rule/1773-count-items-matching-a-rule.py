class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey=='type':
            ind=0
        if ruleKey=='color':
            ind=1
        if ruleKey=='name':
            ind=2
        count=0
        for i in items:
                if i[ind]==ruleValue:
                    count+=1

        return count
            
        