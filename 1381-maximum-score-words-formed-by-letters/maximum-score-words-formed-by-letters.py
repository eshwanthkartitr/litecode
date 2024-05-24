class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # \U0001f911
        
        # mp=[]
        # for i in words:
        #     result=0
        #     for j in i:
        #         result += score[ord(j)-ord('a')]
        #     mp.append((i,result))
        # mp=sorted(mp,key=lambda x:x[1],reverse = True)
        # res=0
        # print(mp)
        # for i in mp:
        #     sub_tho=letters
        #     k=0
        #     for j in i[0]:
        #         if j in letters:
        #             sub_tho.remove(j) 
        #         else:
        #             k=1
        #     if k == 0:
        #         letters = sub_tho 
        #         res+=i[1]
        # return res
        def get_score(word):
            return sum(score[ord(c) - ord('a')] for c in word)

        def backtrack(idx, curr_cnt, curr_score):
            nonlocal max_score
            if idx == len(words):
                max_score = max(max_score, curr_score)
                return

            word = words[idx]
            word_cnt = Counter(word)
            if all(word_cnt[c] <= curr_cnt[c] for c in word_cnt):
                for c in word_cnt:
                    curr_cnt[c] -= word_cnt[c]
                backtrack(idx + 1, curr_cnt, curr_score + get_score(word))
                for c in word_cnt:
                    curr_cnt[c] += word_cnt[c]

            backtrack(idx + 1, curr_cnt, curr_score)

        cnt = Counter(letters)
        max_score = 0
        backtrack(0, cnt, 0)
        return max_score