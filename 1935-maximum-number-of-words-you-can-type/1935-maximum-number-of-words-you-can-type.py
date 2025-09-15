class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        tmp = [1] * len(words)
        n = len(words)
        for i in range(n):
            for m in brokenLetters:
                if m in words[i]:
                    tmp[i] = 0
        

        return sum(tmp)
