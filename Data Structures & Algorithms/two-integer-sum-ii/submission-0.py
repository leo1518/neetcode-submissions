class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = sorted(numbers)
        left = 0
        right = len(nums)-1
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                return [left+1,right+1]