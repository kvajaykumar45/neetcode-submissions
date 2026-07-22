class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        twenty = 0
        for each in bills:
            if each == 5:
                five += 5
            elif each == 10:
                if five >= 5:
                    five -= 5
                    ten += 10
                else:
                    return False
            elif each == 20:
                if (five >= 5 and ten >= 10):
                    five -= 5
                    ten -= 10
                    twenty += 20
                elif  five >= 15:
                    five -= 15
                    twenty += 20
                else:
                    return False
        return True


        