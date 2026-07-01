class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        e = 0
        for i in range(len(nums)):
            multi = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                multi = nums[j] * multi
            output.append(multi)
        return output