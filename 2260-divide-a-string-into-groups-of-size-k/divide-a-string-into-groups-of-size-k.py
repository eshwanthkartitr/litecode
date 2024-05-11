class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        final=[]
        for i in range(0,n,k):
            result=[]
            for j in range(k):
                if i+j >= n:
                    result.append(fill)
                else:
                    result.append(s[i+j])
            final.append("".join(result))
        return final