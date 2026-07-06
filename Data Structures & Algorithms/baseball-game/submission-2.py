class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        total = 0
        for each in operations:
            if each == '+':
                s = record[-1] + record[-2]
                record.append(s)
                total += s
            elif each == "D":
                s = record[-1] * 2
                record.append(s)
                total += s
            elif each == "C":
                total = total - record.pop()
            else:
                s = int(each)
                record.append(s)
                total += s
        return total
        