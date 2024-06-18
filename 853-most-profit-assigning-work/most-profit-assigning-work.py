class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        mp=sorted(zip(difficulty,profit))
        worker.sort()
        u=0
        ma=0
        j=0
        for i in range(len(worker)):
            while j < len(mp) and worker[i] >= mp[j][0]:
                ma= max(ma,mp[j][1])
                j+=1
            u +=ma 
        return u