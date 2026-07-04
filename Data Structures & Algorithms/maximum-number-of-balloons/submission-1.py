class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target="balloon"
        freq = {}
        for each in text:
            if each in target:
                freq[each] = freq.get(each, 0) + 1
        return min(freq.get('b',0), freq.get('a',0), freq.get('l',0)//2, freq.get('o',0)//2, freq.get('n',0))       