class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score=[]
        for i in operations:
            if i =='+' and len(score)>1:
                score.append(score[-1]+score[-2])
            elif i =='D' and len(score)>0:
                score.append(2*score[-1])
            elif i =='C':
                score.pop()
            else:
                try:
                    score.append(int(i))
                except (error):
                    continue

        return sum(score)
