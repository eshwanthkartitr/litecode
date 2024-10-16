class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        mp=[["a",a],["b",b],["c",c]]
        result=""
        while True:
            mp.sort(key=lambda x:-x[1])
            if mp[0][1]==0:
                break
            if len(result)>=2 and result[-1]==result[-2] == mp[0][0]:
                if mp[1][1]==0:
                    break
                result+=mp[1][0]
                mp[1][1]-=1
            else:
                result+=mp[0][0]
                mp[0][1]-=1
        return result