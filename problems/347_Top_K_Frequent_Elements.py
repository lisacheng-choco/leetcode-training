'''
- Leetcode URL: https://leetcode.com/problems/top-k-frequent-elements/
'''

from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def solution1():
            '''
            create a hashtable key:value= num:count
            sort dict by value

            - time complexity: O(nlogn), n = the length nums
            - space complexity: O(n)
            '''
            temp={}
            for num in nums:
                temp[num] = temp.get(num, 0) + 1

            sorted_list = sorted(temp.items(), key=lambda x:x[1], reverse=True) # decending
            
            ans = []
            for i in range(k):
                ans.append(sorted_list[i][0])
            return ans

        def solution2():
            '''
            create a hashtable key:value= num:count
            use bucket sort to find k most frequent

            - time complexity: O(n)
            - space complexity: O(n)
            '''
            count={}
            freq=[[] for i in range(len(nums)+1)] # index: frequency, value: [num] => bucket sort
            for num in nums:
                count[num] = count.get(num, 0) + 1
            for key, c in count.items():
                freq[c].append(key)
            
            ans = []
            for idx in range(len(freq)-1, -1, -1):
                ans = ans + freq[idx]
                if len(ans) >= k:
                    return ans


        return solution2()

nums = [1,1,1,2,2,3]
k = 2
S = Solution()
print(S.topKFrequent(nums, k))