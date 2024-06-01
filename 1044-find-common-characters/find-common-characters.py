class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        wow=[]
        chars = set(words[0])
        for char in chars:
            freq = min([word.count(char) for word in words])
            wow += freq*[char]
        return wow