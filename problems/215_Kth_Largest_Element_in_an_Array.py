from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def solution1():
            '''
            First, build a heap, O(n)
            Second, heappop, O(log n), for k times, so it is O(k log n) 

            - time complexity: O(k log n) 
            - space complexity: O(1)
            '''
            return heapq.nlargest(k, nums)[-1]
        
        def solution2():
            '''
            create a minHeap with size of k
            use nums[0] to get the root node, which is the kth largest in the nums

            - time complexity: O(n * log k)
            '''
            minHeap = []
            for e in nums:
                if len(minHeap) <=k:
                    minHeap.append(e)
                    heapq.heapify(minHeap)
                
                if minHeap[0] > e:
                    pass
                else:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, e)
                    
            return minHeap[0]
        
        def solution3(arr, l, r, k):
            """
            quick sort
            """
            k = len(nums) - k
            pivot_val = arr[r]
            partition_idx = l

            for i in range(l, r):
                if arr[i] <= pivot_val:
                    arr[i], arr[partition_idx] = arr[partition_idx], arr[i]
                    partition_idx += 1
                
            # move pivot to its final place
            arr[partition_idx], arr[r] = arr[r], arr[partition_idx]

            if partition_idx < k:
                return solution3(arr, partition_idx+1, r, k)
                
            elif partition_idx > k:
                return solution3(arr, l, partition_idx-1, k)
            else:
                return arr[k]


        return solution3(nums, 0, len(nums)-1, k) 
        # return solution1()

nums = [3,2,1,5,6,4]
k = 2
s = Solution()
print (s.findKthLargest(nums, k))
