class Solution:

    def encode(self, strs: List[str]) -> str:
        a=""
        for c in strs:
            a+=str(len(c))+ "#" +c
        return a
        

    def decode(self, s: str) -> List[str]:
        a=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            leng=int(s[i:j])
            b=s[j+1:j+leng+1]
            a.append(b)
            i=j+1+leng
        return a

