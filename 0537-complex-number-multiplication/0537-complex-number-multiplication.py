class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a1,b1 = num1.split("+")
        a2,b2 = num2.split("+")
        re = int(a1)*int(a2)-int(b1[:-1])*int(b2[:-1])
        img = int(a1)*int(b2[:-1])+int(b1[:-1])*int(a2)
        return str(re)+"+"+str(img)+"i"