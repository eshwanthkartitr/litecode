class Solution:
    def twoEditWords(self, queries: List[str], dic: List[str]) -> List[str]:
        re=[]
        for i in queries:
            fall = False
            for j in dic:
                m=0
                cnt =0
                sizee=len(i)
                while m<sizee:
                    if i[m]==j[m]:
                        cnt+=1
                    if cnt>=sizee-2:
                        fall=True
                        break
                        
                    m+=1
                
                if fall or cnt>=sizee-2:
                    re.append(i)
                    break

        return re