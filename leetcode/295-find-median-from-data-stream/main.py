class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []  # Prefer items to be in this heap
        self.min_heap = []
        
    def addNum(self, num: int) -> None:
        if not self.min_heap or not self.max_heap:
            heapq.heappush(self.max_heap, -1 * num)
            self.rebalance_heaps()
            return
        min_val, max_val = -1 * self.max_heap[0], self.min_heap[0]
        if num <= min_val:
            heapq.heappush(self.max_heap, -1 * num)
        else:
            heapq.heappush(self.min_heap, num)
        self.rebalance_heaps()
            
    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -1 * self.max_heap[0]
        else:
            return (self.min_heap[0] + -1 * self.max_heap[0]) / 2
        
    def rebalance_heaps(self):
        while len(self.max_heap) - len(self.min_heap) - 1 > 0:
            value = -1 * heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, value)
        while len(self.min_heap) - len(self.max_heap) > 0:
            value = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -1 * value)
        

