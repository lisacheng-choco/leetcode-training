'''
- Leetcode URL: https://leetcode.com/problems/last-stone-weight/
'''
from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        use heap to keep list sorted after stone pop and push operation

        - time complexity: O(nlog n)
        - space complexity: O(n)
        '''
        minHeap = [ -1* e for e in stones]
        heapq.heapify(minHeap)
        
        while len(minHeap) > 1:
            
            y = heapq.heappop(minHeap) * -1
            x = heapq.heappop(minHeap) * -1
            remain = y - x
            if remain > 0:
                heapq.heappush(minHeap, remain * -1)

        if len(minHeap) == 0:
            return 0
        else:
            return heapq.heappop(minHeap) * -1


input = [2,7,4,1,8,1]
s = Solution()

print(s.lastStoneWeight(input))