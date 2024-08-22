class Solution:
    def findComplement(self, num: int) -> int:
        re = bin(num)[2:]
        re=list(re)
        for i in range(len(re)):
            if re[i]=="1":
                re[i]="0"
            else:
                re[i]="1"
        return int("".join(re),2)