class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_var=0
        ten_var=0
        for i in bills:
            if i==5:
                five_var+=1
            if i==10:
                ten_var+=1
                five_var-=1
            if i == 20:
                print(five_var,ten_var)
                if ten_var>=1 and five_var>=1:
                    ten_var-=1
                    five_var-=1
                elif five_var>=3:
                    five_var-=3
                else:
                    return False
        return True
