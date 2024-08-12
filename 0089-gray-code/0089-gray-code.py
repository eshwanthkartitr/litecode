class Solution:
    def grayCode(self, n: int) -> List[int]:
        def helper(n):
            if n<=0:
                return ["0"]
            if n==1:
                return ["0","1"]
            myrec = helper(n-1)
            rec=[]
            for i in myrec:
                rec.append('0'+i)
            for i in myrec[::-1]:
                rec.append('1'+i)
            return rec
        hi = helper(n)
        re=[]
        for i in hi:
            re.append(int(i,2))
        return re