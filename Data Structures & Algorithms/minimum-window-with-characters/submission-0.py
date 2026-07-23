class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        start=0
        left=0
        minl= float("inf")
        seen={}
        need={}
        have=0
        for c in t:
            seen[c]=seen.get(c,0)+1
        for right in range(len(s)):
            a= s[right]
            if a in seen:
                need[a]=need.get(a,0)+1
                if need[a]==seen[a]:
                    have+=1
            while have==len(seen):
                if right-left+1<minl:
                    minl=right-left+1
                    start=left
                leftc =s[left]
                if leftc in seen:
                    need[leftc]-=1
                    if need[leftc]<seen[leftc]:
                        have-=1
                left+=1
        if minl==float("inf"):
            return ""
        return s[start:start+minl]
                

        