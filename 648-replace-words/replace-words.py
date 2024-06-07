class Solution:
    def replaceWords(self, d: List[str], sentence: str) -> str:
        re=[]
        los = sentence.split(" ")
        cnt=0
        d = set(d)
        for i in los:
            for j in range(1,len(i)):
                if i[0:j] in d:
                    los[cnt]=i[0:j]
                    break
            cnt+=1
        return " ".join(los)