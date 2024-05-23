class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        myDict=defaultdict(int)
        for i in emails:
            local,domain = i.split('@')
            local = local.split('+')[0]
            local = local.replace('.','')
            myDict[local+'@'+domain]+=1
        return len(myDict)
