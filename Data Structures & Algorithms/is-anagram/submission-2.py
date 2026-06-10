class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = list(s)
        list2 = list(t)
        list1.sort()
        list2.sort()
        if len(s) != len(t):
                return False
        for i in range(len(s)):
            if list1[i] != list2[i]:
                return False
        return True
            
