class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d={}
        for c in nums:
            d[c]=d.get(c,0)+1
        for i in d.values():
            if i>1:
                return True
        
        return False
        

        