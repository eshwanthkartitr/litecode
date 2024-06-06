class Solution:
    def partitionString(self, s: str) -> int:
        #re=[[]]
        #for i in s:
        #    if i not in re[-1]:
        #        re[-1].append(i)
        #    else:
        #        re.append([i])
        #return len(re)
        uni=set()
        c=1
        for i in s:
            if i in uni:
                c+=1
                uni=set()
            uni.add(i)
        return c