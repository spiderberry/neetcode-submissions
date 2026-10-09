class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        vistedNum = set()

        for num in nums:
            if num in vistedNum:
                return True
            
            vistedNum.add(num)

        return False