class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low <= high:
            mid = (low + high)//2
            hrs = 0
            for each in piles:
                hrs += (each + mid - 1) // mid
            if hrs <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low