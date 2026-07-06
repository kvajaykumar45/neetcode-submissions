class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for each in operations:
            if each == '+':
                s = record[-1] + record[-2]
                record.append(s)
            elif each == "D":
                s = record[-1] * 2
                record.append(s)
            elif each == "C":
                record.pop()
            else:
                record.append(int(each))
        return sum(record)
        