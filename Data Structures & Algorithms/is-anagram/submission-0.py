class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a={}
        b={}
        for c in s:
            a[c]=a.get(c,0)+1
        for d in t:
            b[d]=b.get(d,0)+1
        if a==b:
            return True
        return False

        