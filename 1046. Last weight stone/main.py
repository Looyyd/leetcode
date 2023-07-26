from typing import List
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)

        while (len(heap)) > 1 :
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            if a==b:
                continue
            else:
                heapq.heappush(heap, (a-b))

        if len(heap) == 0:
            return 0
        else:
            return -1 * heap[0]

