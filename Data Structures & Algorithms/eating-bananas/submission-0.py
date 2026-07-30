class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        
        while left<=right:
            k=(left+right)//2
            su=0

            for x in piles:
                su+=math.ceil(x/k)
            if su>h:
                left=k+1
            else:
                right=k-1
        return left

                


        