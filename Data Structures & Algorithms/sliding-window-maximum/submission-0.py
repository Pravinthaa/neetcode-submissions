class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left=0
        window=[]
        maxl=[]
        for right in range(len(nums)):
            a=nums[right]
            window.append(a)
            while right-left+1>k:
                ab=nums[left]
                window.remove(ab)
                left+=1
            if right-left+1==k:
                maxl.append(max(window))
        return maxl


        