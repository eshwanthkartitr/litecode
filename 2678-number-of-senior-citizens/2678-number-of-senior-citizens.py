import re
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt=0
        for i in details:
            tst = re.findall("[M,F](\d+)",i)
            if int(tst[0][:2]) > 60:
                cnt+=1
        return cnt