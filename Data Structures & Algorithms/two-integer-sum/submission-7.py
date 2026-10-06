class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        checkedNums = {}

        for i, j in enumerate(nums):
            diff = target - j

            if diff in checkedNums:
                return [checkedNums[diff], i]

            checkedNums[j] = i