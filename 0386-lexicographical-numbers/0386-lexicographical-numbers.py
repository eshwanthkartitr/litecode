class Solution:
    def dfs(self,n,cur,re):
        if cur>n:
            return
        re.append(cur)
        self.dfs(n,cur*10,re)
        if cur % 10 != 9:
            self.dfs(n,cur+1,re)
        return re

    def lexicalOrder(self, n: int) -> List[int]:
        res=[]
        return self.dfs(n,1,res)