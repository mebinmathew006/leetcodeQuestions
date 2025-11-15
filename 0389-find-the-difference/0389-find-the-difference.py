class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        di={}
        for i in s:
            if i in di:
                di[i]+=1
            else:
                di[i]=1
        dii={}
        for i in t:
            if i in dii:
                dii[i]+=1
            else:
                dii[i]=1
        for i in t:
            try:
                if dii[i]:
                    pass
                if di[i] != dii[i]:
                    return i
            except Exception as e:
                return i