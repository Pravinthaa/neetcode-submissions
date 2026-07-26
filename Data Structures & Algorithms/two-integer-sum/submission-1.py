class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for c in range(len(nums)):
            a=target-nums[c]
            if a in d:
                return [d[a],c]
            d[nums[c]]=c


        