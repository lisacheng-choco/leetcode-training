'''
- Leetcode URL: https://leetcode.com/problems/k-closest-points-to-origin/
'''

import collections
from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def solution1():
            '''
            iterate over the points and calculate distances
            use minHeap to keep the order of distances

            n is the length of points
            - time complexity: O(n) + O(k log n) = O(k log n)
            - space complexity: O(n)
            '''
            disList = []
            disDict = collections.defaultdict(list)
            ans = []
                
            for i in range(len(points)): 
                point = points[i]
                x, y = point[0], point[1]
                dis = x**2 + y**2

                disList.append(dis)
                disDict[dis].append(i)

            heapq.heapify(disList) # time complexity: O(n)

            for k in range(k):  # time complexity: k * O(log n)
                kdis = heapq.heappop(disList) 
                point = points[disDict[kdis].pop()]
                ans.append(point)

            return ans
        
        def solution2():
            disList = []
            ans = []
            for e in points:
                dis = e[0]**2 + e[1]**2
                disList. append((dis, e))
            
            heapq.heapify(disList)

            i = 0
            while i < k:  # time complexity: k * O(log n)
                dis, e = heapq.heappop(disList) 
                ans.append(e)
                i += 1
            
            return ans
        
        def solution3():
            '''
            iterate over the points and calculate distances
            use list of tuples, tuple is to store distance and point
            sort tuple by the first index
            return top k points

            n is the length of points
            - time complexity: O(n log n)
            - space complexity: O(n)
            '''
            disList = []
            for e in points: # time complexity: O(n)
                disList.append((e[0]**2 + e[1]**2, e))
            disList.sort(key=lambda tup: tup[0]) # time complexity: O(n log n)
            return [tup[1] for tup in disList[:k] ]
            
            
        return solution3()

points = [[3,3],[5,-1],[-2,4]]
k = 2
s = Solution()
print(s.kClosest(points, k))

