class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxlevel = 0
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            water = height*width
            if water > maxlevel:
                maxlevel = water
            if heights[left] < heights[right]:
                left = left + 1
            else:
                right = right - 1
        return maxlevel


        