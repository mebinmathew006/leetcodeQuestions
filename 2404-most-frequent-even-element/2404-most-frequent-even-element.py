class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        dicts={}
        for i in nums:
            if i%2==0:
                if i in dicts:
                    dicts[i]+=1
                else:
                    dicts[i]=1

        if len(dicts)==0:
            return -1
        

        largest=max(dicts.values())
        keys=float('-inf')
        li=[]
        for k,v in dicts.items():
            if largest == v:
                li.append(k)


        return min(li)


        
       
