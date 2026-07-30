class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i - 1] == num:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                curSum = num + nums[j] + nums[k]
                if curSum < 0:
                    j += 1
                elif curSum > 0:
                    k -= 1
                else:
                    res.append([num, nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j - 1] == nums[j]:
                        j += 1
        return res

