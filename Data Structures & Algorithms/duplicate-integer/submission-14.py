class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        visitedNums = set()

        for i in nums:
            if i in visitedNums:
                return True
            
            visitedNums.add(i)
            
        return False