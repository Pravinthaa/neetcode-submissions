class Solution:
    def trap(self, height: List[int]) -> int:
        total=0
        for i in range(1,len(height)-1):
            l=max(height[0:i])
            r=max(height[i+1:])
            water=min(l,r)-height[i]
            if water>0:
                total+=water
        return total