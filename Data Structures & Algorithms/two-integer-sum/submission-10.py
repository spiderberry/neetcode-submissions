class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        checkedNums = {}

        for index in range(len(nums)):
            diff = target - nums[index]

            if diff in checkedNums:
                return [checkedNums[diff], index]

            checkedNums[nums[index]] = index