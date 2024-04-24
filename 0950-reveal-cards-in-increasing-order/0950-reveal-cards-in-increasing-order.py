class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        re=[0]*n
        li=[i for i in range(n)]
        for card in deck:
            temp = li.pop(0)
            re[temp]=card
            if li:
                li.append(li.pop(0))
        return re 