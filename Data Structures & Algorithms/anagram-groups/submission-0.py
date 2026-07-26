class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for words in strs:
            a="".join(sorted(words))
            if a not in d:
                d[a]=[]
            d[a].append(words)
        return list(d.values())

        