class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        tar = mean*(n+len(rolls)) - sum(rolls)
        if tar < n or tar > 6 * n:
            return []
        re=[tar//n]*n
        i=0
        cur_sum=sum(re)
        while cur_sum<tar:
            change = min(6 - re[i], tar - cur_sum)
            re[i] += change
            cur_sum+=change
            i=(i+1)%n
        return re