class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num, freq in count.items():
            frequency[freq].append(num)

        res = []
        for freq in range(len(nums), 0, -1):

            for num in frequency[freq]:
                res.append(num)
                if len(res) == k:
                    return res