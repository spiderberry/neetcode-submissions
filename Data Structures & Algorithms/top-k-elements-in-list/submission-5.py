class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for number, occur in count.items():
            freq[occur].append(number)

        res = []

        for occur in range(len(freq) - 1, 0, -1):
            for num in freq[occur]:
                res.append(num)

                if len(res) == k:
                    return res