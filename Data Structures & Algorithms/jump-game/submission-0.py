class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        r = len(nums) - 1
        l = r - 1
        while r > 0:
            while l >= 0:
                if nums[l] >= r - l:
                    r = l
                    l = r - 1
                    break
                l -= 1
                if l < 0: return False
        return True
