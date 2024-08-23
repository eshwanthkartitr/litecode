from fractions import Fraction
class Solution:
    def fractionAddition(self, expression: str) -> str:
        Farc = []
        num=""
        for i in expression:
            if i in "+-":
                if num:
                    Farc.append(num)
                num=i
            else:
                num+=i
        Farc.append(num)
        total = Fraction(0)
        for i in Farc:
            total+=Fraction(i)
        return str(total) if len(str(total)) != 1 else str(total)+'/1'