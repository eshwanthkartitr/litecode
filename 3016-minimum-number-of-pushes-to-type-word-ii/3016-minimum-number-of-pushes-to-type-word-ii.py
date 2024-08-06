class Solution:
    def minimumPushes(self, word: str) -> int:
        hi = sorted(word,key=lambda x:word.count(x),reverse=True)
        visited = set()
        lev=0
        su=0
        for i in range(len(hi)):
            if hi[i] not in visited:
                lev = (len(visited)//8)+1
                su+=lev*word.count(hi[i])
                visited.add(hi[i])
        return su