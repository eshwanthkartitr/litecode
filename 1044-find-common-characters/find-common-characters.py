class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        wow=[] 
        for i in range(len(words)): 
            wow.append(set(words[i]))
        mp=defaultdict(list)
        for i in range(len(wow)):
            for j in wow[i]:
                mp[j].append(words[i].count(j))
        print(mp)
        re=[]
        for i in mp.keys():
            if len(mp[i]) == len(words):
                for j in range(min(mp[i])):
                    re.append(i)
        re.sort()
        return re