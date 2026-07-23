class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        seen=set()
        maxl=0

        for right in range(len(s)):
            ch=s[right]
            
            while ch in seen:
                ab=s[left]
                seen.remove(ab)
                left+=1
            seen.add(s[right])
            maxl=max(maxl,right-left+1)
        return maxl


        