class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2 :
            return True
        if len(s1)==1 :
            if s1==s2:
                return True
            else:
                return False
        if len(s1)==2:
            if s1 == s2[1]+s2[0]:
                return True
            else :
                return False
        left  = 0
        count =0
        first=second =None
        flag=None
        while left<len(s1):
            if s1[left]!=s2[left]:
                count+=1
                if count ==1:
                    first = left
                elif count ==2:
                    second =left
                else:
                    flag= False
            left+=1

        if flag==None:
            flag= True
        if flag == True:
            if sorted(s1)==sorted(s2):
                return True
            
        return False
