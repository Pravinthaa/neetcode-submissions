class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        a=1
        long=1
        
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                continue
            elif nums[i-1]+1==nums[i]:
                a+=1
            else:
                a=1
            long=max(a,long)
        if len(nums)==0:
            return 0
        return long
        