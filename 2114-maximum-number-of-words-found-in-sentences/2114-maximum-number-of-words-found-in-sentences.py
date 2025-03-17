class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        hs={}
        for i in sentences:
            hs[i]=len(i.split(' '))

        return max(hs.values())