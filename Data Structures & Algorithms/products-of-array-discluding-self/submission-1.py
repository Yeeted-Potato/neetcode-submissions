class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multi, zero_count = 1, 0
        output = []
        for i in nums:
            if i:
                multi *= i
            else:
                zero_count += 1
        
        if zero_count > 1: return [0] * len(nums)

        output = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_count:
                if c == 0:
                    output[i] = multi
                else:
                    output[i] = 0
            else:
                final = multi // nums[i]
                output[i] = final
        return output