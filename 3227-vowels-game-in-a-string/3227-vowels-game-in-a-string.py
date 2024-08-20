class Solution:
    def doesAliceWin(self, s: str) -> bool:
        for i in ['a','e','i','o','u']:
            if s.count(i)>0:
                return True
        return False