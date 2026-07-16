class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            rest = target - nums[i]
            if nums[i] in hashmap:
                return [hashmap[nums[i]], i]
           
            hashmap[rest] = i
\