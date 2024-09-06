class Solution:
    def sortVowels(self, s: str) -> str:
        st =['a','e','i','o','u','A','E','I','O','U']
        s=list(s)
        re=[]
        for i in range(len(s)):
            if s[i] in st:
                re.append(s[i])
        re.sort()
        i=0
        for j in range(len(s)):
            if s[j] in st:
                s[j]=re[i]
                i+=1
        print(s)
        return "".join(s)
                