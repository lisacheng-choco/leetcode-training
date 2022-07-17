'''
- Leetcode URL: https://leetcode.com/problems/product-of-array-except-self/
'''

from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        def solution1():
            '''
            use nested for loops

            - time complexity: O(n^2)
            - space complexity: O(n)
            '''
            ans = []
            for i in range(len(nums)):
                m = 1
                for j in range(len(nums)):
                    if i == j:
                        continue
                    m = m * nums[j]
                ans.append(m)

            return ans
        
        def solution2():
            '''
            - time complexity: O(n)
            - space complexity: O(n)
            '''
            prefix, postfix = [1], [1]

            curr = 1
            for i in range(len(nums)):
                prefix.append(nums[i]*curr)
                curr = nums[i]*curr

            curr = 1
            for j in range(len(nums)-1, -1, -1):
                curr = nums[j]*curr
                postfix = [curr]+postfix

            return [prefix[k]*postfix[k+1] for k in range(len(nums))]


        def solution3():
            '''
            - time complexity: O(n)
            - space complexity: O(1)
            '''
            prefix, postfix = 1 ,1
            res = [1] * len(nums)

            for i in range(len(nums)):
                res[i] = prefix
                prefix *= nums[i]

            for j in range(len(nums)-1, -1, -1):
                res[j] *= postfix
                postfix *= nums[j] 

            return res

        return solution3()

nums = [1,2,3,4]
s = Solution()
print(s.productExceptSelf(nums))
        