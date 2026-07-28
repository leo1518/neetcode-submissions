class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(path,count,start):
            if count >= target:
                if count == target:
                    res.append(path[:])
                return 
            for i in range(start,len(nums)):
                path.append(nums[i])
                helper(path,count+nums[i],i)
                path.pop()
        helper([],0,0)
        return res