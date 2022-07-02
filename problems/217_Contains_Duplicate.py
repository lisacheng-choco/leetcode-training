'''
- Leetcode URL: https://leetcode.com/problems/contains-duplicate/
- Video: https://www.youtube.com/watch?v=3OamzN90kPg
'''
class Solution:
    def containsDuplicate(self, nums) -> bool:
        
        def solution1():
            '''
            iterate numbers in list and use hashtable to record the known numbers as True 
            so that we can identify the number if duplicated or not

            - time complexity: O(n)
            - space complexity: O(n)
            '''
            temp = {}
            for n in nums:
                if temp.get(n) is None:
                    temp[n] = True
                else:
                    return True
            return False
        
        def solution2():
            '''
            iterate numbers in list and use hashset to record the known numbers as True 
            so that we can identify the number if duplicated or not

            - time complexity: O(n)
            - space complexity: O(n)
            '''
            hashset = set()
            for n in nums:
                if n in hashset:
                    return True
                else:
                    hashset.add(n)
            return False
            
        def solution3():
            '''
            First, to sort the list
            Second, use two pointers to take a number and its neighbor to compare is duplicated or not

            - time complexity: O(nlogn)
            - space complexity: O(1)
            '''
            nums.sort() # time: O(nlogn)
            prev = None
            for curr in nums: # time: O(n)
                if prev is None:
                    prev = curr
                else:
                    if prev == curr:
                        return True

            return False

        

        return solution2()

   
nums = [1,2,3,1]     
s = Solution()
print(s.containsDuplicate(nums))