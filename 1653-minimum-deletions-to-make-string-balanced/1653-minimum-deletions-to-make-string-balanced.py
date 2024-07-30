class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_cnt = [0]*len(s)
        for i in range(len(s)-2,-1,-1):
            if s[i+1]=="a":
                a_cnt[i] = a_cnt[i+1]+1
            else:
                a_cnt[i] = a_cnt[i+1]+0
        print(a_cnt)
        b_cnt_left = 0
        res = len(s)
        for i,c in enumerate(s):
            res = min(res,b_cnt_left+a_cnt[i])
            if c == "b":
                b_cnt_left+=1
        return res