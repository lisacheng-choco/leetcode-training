'''
- Leetcode URL: https://leetcode.com/problems/kth-largest-element-in-a-stream/
'''

from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        '''
        N: the length of nums
        M: the number of calls to add()
        time complexity: O(N*log N + M*log k)
        space complexity: O(N)
        '''

        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap) # O(N)
        while len(self.minHeap)  > k: 
            # the number of pop() = k-n, the worst case = k-1, nearly n
            # O(N*log N)
            heapq.heappop(self.minHeap)
        # time complexity: O(N) + O(N*log N) = O(N*log N)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) # O(log(k))
        if len(self.minHeap)  > self.k:
            heapq.heappop(self.minHeap) # O(log(k))
        return self.minHeap[0]
        # time complexity: O(log(k)) + O(log(k)), nearly O(log k) for add()


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)