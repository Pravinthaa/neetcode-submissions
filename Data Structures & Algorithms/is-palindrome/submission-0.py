class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        words=""
        for c in s:
            if c.isalnum():
                words+=c
        words=words.lower()
        right=len(words)-1
        while left<right:
            if words[left]!=words[right]:
                return False
            left+=1
            right-=1
        return True
        


        