class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        left = 0
        right = n - 1
        boats = 0
        while left <= right:
            wt = people[left] + people[right] 
            if wt <= limit:
                boats += 1
                left += 1
                right -= 1
            elif wt > limit:
                boats += 1
                right -= 1
        return boats