class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        result={}
        for i in range(len(words)):
            cur1 = words[i]
            eve1 = []
            odd1 = []
            for k in range(len(cur1)):
                if k%2 == 0:
                    eve1.append(cur1[k])
                else:
                    odd1.append(cur1[k])
            eve1.sort()
            odd1.sort()
            if (tuple(eve1),tuple(odd1)) in result:
                result[(tuple(eve1),tuple(odd1))].append(cur1)
            else:
                result[(tuple(eve1),tuple(odd1))] = [cur1]
        return len(result.keys())