class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = sorted(strs)

        hash = {}
        for i in strs:
            j = "".join(sorted(i))
            hash[j] = hash.get(j, []) + [i]
        return list(hash.values())