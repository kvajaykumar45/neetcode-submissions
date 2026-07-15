class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        
        while j < len(abbr) and i < len(word):
            if abbr[j]. isalpha():
                if abbr[j] != word[i]:
                    return False
                else:
                    j += 1
                    i += 1
            elif abbr[j].isdigit() :
                if abbr[j] == '0':
                    return False
                else:
                    d = 0
                    while j < len(abbr) and abbr[j].isdigit():
                        d = d * 10 + int(abbr[j])
                        j += 1
                    i = i + d
                    if i > len(word):
                        return False
        return i == len(word) and j == len(abbr)