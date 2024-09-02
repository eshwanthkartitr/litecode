class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        i=0
        temp = sum(chalk)
        divi = k - (k//temp)*temp
        print(divi)
        for i in range(len(chalk)):
            print(divi)
            divi = divi - chalk[i]
            if divi<0:
                return i
        return i+1
