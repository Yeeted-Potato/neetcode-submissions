class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        list = {}

        for i in nums:
            list[i] = 1 + list.get(i, 0)
        
        arr = []
        for num, count in list.items():
            arr.append([count, num])
        arr.sort()

        output = []
        while len(output) < k:
            output.append(arr.pop()[1])
        return output