class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        output = []

        for i in nums:
            hash[i] = 1 + hash.get(i, 0)
        hash = sorted(hash, key=hash.get)
        return hash[-k:]