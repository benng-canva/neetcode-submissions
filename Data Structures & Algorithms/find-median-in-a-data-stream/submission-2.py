from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.minHeap = [] # right
        self.maxHeap = [] # left     

    def addNum(self, num: int) -> None:
        heappush(self.maxHeap, -num)

        val = -heappop(self.maxHeap)
        heappush(self.minHeap, val)

        self.rebalance()

    def rebalance(self) -> None:
        if len(self.minHeap) > len(self.maxHeap) + 1:
            val = heappop(self.minHeap)
            heappush(self.maxHeap, -val)
        elif len(self.maxHeap) > len(self.minHeap) + 1:
            val = -heappop(self.maxHeap)
            heappush(self.minHeap, val)

    def findMedian(self) -> float:
        print(self.minHeap)
        print(self.maxHeap)
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return -self.maxHeap[0]
        
        