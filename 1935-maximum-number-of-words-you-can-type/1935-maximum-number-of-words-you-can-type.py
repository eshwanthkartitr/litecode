class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        cnt = 0
        n = len(words)
        for i in range(n):
            for m in words[i]:
                if m in brokenLetters:
                    cnt+=1
                    break
        

        return n - cnt
