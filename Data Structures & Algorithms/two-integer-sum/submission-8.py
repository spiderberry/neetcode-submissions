class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        checkedNums = {}

        for index, val in enumerate(nums):
            diff = target - val

            if diff in checkedNums:
                return [checkedNums[diff], index]
            checkedNums[val] = index 