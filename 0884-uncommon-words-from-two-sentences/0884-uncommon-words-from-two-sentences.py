class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ls1=s1.split(" ")
        ls2=s2.split(" ")
        inter=[]
        for i in ls1:
            if i not in ls2 and ls1.count(i)==1:
                inter.append(i)
        for i in ls2:
            if i not in ls1 and ls2.count(i)==1:
                inter.append(i)
        return inter
        