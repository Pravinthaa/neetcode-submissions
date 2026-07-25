class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maxl=0
        while left<right:
            total= (right-left)*min(heights[left],heights[right])
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
            maxl=max(maxl,total)
        return maxl