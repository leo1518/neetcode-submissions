class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def back(start, path):
            result.append(path[:])
            if start == len(nums):
                return
            for i in range(start,len(nums)):
                path.append(nums[i])
                back(i+1,path)
                path.pop()
        back(0,[])
        return result