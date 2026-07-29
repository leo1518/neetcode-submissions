class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxjump = 0
        for i in range(len(nums)-1):
            maxjump = max(maxjump, nums[i]+i)
            if maxjump <= i:
                return False
        if maxjump < len(nums) -1:
            return False
        return True