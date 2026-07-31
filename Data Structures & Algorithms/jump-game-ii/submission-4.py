class Solution:
    def jump(self, nums: List[int]) -> int:
        minstep = 0
        curstep = 0      
        farthest = 0  

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == curstep:
                minstep += 1
                curstep = farthest

        return minstep