class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        c=1
        d=[]
        for i in range(len(nums)):
            a=math.prod(nums[0:i])
            b=math.prod(nums[i+1:])
            c=a*b
            d.append(c)
        return d


        