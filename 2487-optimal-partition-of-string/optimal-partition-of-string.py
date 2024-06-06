class Solution:
    def partitionString(self, s: str) -> int:
        re=[[]]
        for i in s:
            if i not in re[-1]:
                re[-1].append(i)
            else:
                re.append([i])
        print(re)
        return len(re)