class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        word=[x[0] for x in words]
        return word==list(s)
            
        