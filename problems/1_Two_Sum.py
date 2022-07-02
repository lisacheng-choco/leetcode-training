'''
- Leetcode URL: https://leetcode.com/problems/two-sum/
- Video: https://www.youtube.com/watch?v=KLlXCFG5TnA
'''
from tkinter import N


class Solution:
    def twoSum(self, nums, target: int):
        '''
        Question
            is nums sorted? False
            are there duplicated numbers in a list? True
        '''

        def solution1_not_work():
            '''
            use a hashtable to recorde number and its index
            iterate the number and search for (target-number) in the hash table
            '''
            temp = {}
            for i in range(len(nums)):
                temp[nums[i]] = i
            
            for j in range(len(nums)):
                rest = target - nums[j]

                if nums[j] == rest:
                    continue

                if temp.get(rest):
                    return [j, temp.get(rest)]
        
        def solution1():
            '''
            iterate nums and calaulate the difference(diff) between current num and target
            if cannot fint the diff in hashtable, assign a new pair of key/value(current num/index) to the hashtable

            - time complexity: O(n)
            - space complexity: O(n)
            '''
            temp = {}
            
            for i, num in enumerate(nums):
                diff = target - num
                if diff in temp:
                    return [i, temp[diff]]
                temp[num] = i

        return solution1()

nums = [1,3,4,2]
target = 6
S = Solution()
print(S.twoSum(nums, target))
        