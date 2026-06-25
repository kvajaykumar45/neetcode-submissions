
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = deque(), deque()

        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        
        final = []
        for i in range(len(nums) // 2):
            final.append(pos.popleft())
            final.append(neg.popleft())
        
        return final
        