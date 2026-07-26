class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        a=[]
        for c in nums:
            d[c]=d.get(c,0)+1
        for i in range(k):
            b=max(d,key=d.get)
            a.append(b)
            d.pop(b)
        return a

        