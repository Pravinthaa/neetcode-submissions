class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        seen={}
        maxk=0
        for right in range(len(s)):
            c=s[right]
            seen[c]=seen.get(c,0)+1

            while (right - left + 1) - max(seen.values()) > k:
                seen[s[left]] -= 1
                left += 1
            maxk=max(maxk,right-left+1)
        return maxk
            

        