class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for j in range(len(nums)):
            needed = target - nums[j]
            if needed in hash:
                return [hash[needed], j]
            hash[nums[j]] = j
        return []
        