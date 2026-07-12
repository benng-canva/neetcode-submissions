from heapq import heappush, heappop, heapify

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []

        for num in count.keys():
            heappush(heap, (count[num], num))
            if len(heap) > k:
                heappop(heap)

        result = []
        while len(heap) > 0:
            result.append(heappop(heap)[1])

        return result
        