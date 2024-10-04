class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        su=0
        for i in range(len(skill)//2):
            if skill[i]+skill[len(skill)-i-1]!=skill[0]+skill[-1]:
                return -1
            su += skill[i]*skill[len(skill)-i-1]
        return su