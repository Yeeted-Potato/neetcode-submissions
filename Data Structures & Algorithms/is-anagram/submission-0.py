class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortedS = sorted(s)
        sortedT = sorted(t)

        for i in range(len(sortedS)):
            if sortedS != sortedT:
                return False
            else:
                continue
        return True