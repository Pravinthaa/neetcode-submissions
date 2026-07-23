class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen={}
        need={}
        for c in s1:
            seen[c]= seen.get(c,0)+1
        left=0
        if len(s1)>len(s2):
            return False
        for right in range(len(s2)):
            a=s2[right]
            need[a]=need.get(a,0)+1
            

            while right-left+1>len(s1):
                ab=s2[left]
                need[ab]-=1
                left+=1
                if need[ab]==0:
            
                    del need[ab]
            if need==seen:
                return True

        return False

        