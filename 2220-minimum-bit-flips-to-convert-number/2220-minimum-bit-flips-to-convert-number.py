class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        x,y=list(bin(start)[2:]),list(bin(goal)[2:])
        if len(bin(start))>len(bin(goal)):
            y = ['0'] * (len(bin(start))-len(bin(goal)))+y
        else:
            x=['0'] * (-len(bin(start))+len(bin(goal)))+x
        su=0
        print(x,y)
        for i in range(len(x)):
            if x[i]!=y[i]:
                su+=1
        return su