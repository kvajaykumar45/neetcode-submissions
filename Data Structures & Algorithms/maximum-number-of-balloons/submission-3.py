class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target={'b','a','l','o','n'}
        freq = Counter(ch for ch in text if ch in target)
        return min(freq.get('b',0), freq.get('a',0), freq.get('l',0)//2, freq.get('o',0)//2, freq.get('n',0))
       