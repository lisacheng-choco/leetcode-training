'''
- Leetcode URL: https://leetcode.com/problems/valid-sudoku/
'''
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def solution1():
            '''
            sort nums and update the maximun lenght of consecutive sequence

            - time complexity: O(nlog n) (because of sort finction)
            - space complexity: O(1)
            '''
            if len(nums) == 0:
                return 0
            
            nums.sort()
            curr_length, max_length = 1, 1
            curr_num = nums[0]
            prev_num = curr_num
            for num in nums:
                prev_num = curr_num
                curr_num = num
                if abs(curr_num-prev_num) == 1:
                    curr_length += 1
                elif abs(curr_num-prev_num) == 0:
                    pass
                else:    
                    max_length = curr_length if curr_length>max_length else max_length
                    curr_length = 1
            return curr_length if curr_length>max_length else max_length

        def solution2():
            '''
            創造新的number問問nums有沒有
            1. iterate each number in nums to check if it is the beginning of a subsequence by " if (num-1) in nums "
            2. if yes, find the next number until we cannot find new number anymore

            - time complexity: O(n)
            - space complexity: O(n)
            - n is length of nums 
            '''
            numSet = set(nums)
            longest = 0
            
            for n in nums:
                if (n-1) not in numSet:
                    curr_length = 0
                    while (n + curr_length) in numSet:
                        curr_length +=1
                    longest = max(longest, curr_length)
            return longest
        
        return solution2()

nums = [1,2,0,1] #[0,3,7,2,5,8,4,6,0,1] #[100,4,200,1,3,2]
s = Solution()
print(s.longestConsecutive(nums))