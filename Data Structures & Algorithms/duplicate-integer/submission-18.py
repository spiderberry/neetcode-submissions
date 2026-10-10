class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        numsVisited = set()

        for num in nums:
            if num in numsVisited:
                return True
            numsVisited.add(num)
        return False