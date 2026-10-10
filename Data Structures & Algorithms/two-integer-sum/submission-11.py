class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        checked = {}

        for index in range(len(nums)):

            diff = target - nums[index]
            
            if diff in checked:
                return [checked[diff], index]

            checked[nums[index]] = index
