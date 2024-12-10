class Solution:
    def maximumLength(self, s: str) -> int:
        mp=defaultdict(int)
        n=len(s)
        for i in range(n):
            for j in range(i+1,n+1):
                if len(set(s[i:j]))<2:
                    mp[s[i:j]]+=1
        max_l = 0
        for i,j in mp.items():
            if j>=3:
                max_l = max(max_l,len(i))
        return max_l if max_l!=0 else -1
