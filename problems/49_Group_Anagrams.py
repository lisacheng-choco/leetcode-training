'''
- Leetcode URL: https://leetcode.com/problems/group-anagrams/
'''

from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def solution1():
            '''
            iterate the strs and sort easch elemernt
            create a hashtable key/value = sorted str/[original str]

            - time complecity: O(m * nlogn), m: the length of strs(list), n: the avg length of str 
            - space complexity: O(m)
            '''
            temp = {}
            for s in strs:
                sorted_s = "".join(sorted(s))
                # temp[sorted_s] = temp.get(sorted_s, []).append(s)
                temp[sorted_s] = temp.get(sorted_s, [])
                temp[sorted_s].append(s)

            return [temp[k] for k in temp]
        

        def solution2():
            '''
            iterate the strs and count character for each str
            create a hashtable key/value = count list/[original str]

            - time complexity: O(m * n), m: the length of strs(list), n: the avg length of str
            - space complexity: O(m)
            '''
            temp = {}
            for s in strs:
                char_count = [0] * 26

                for c in s:
                    char_count[ord(c) - ord("a")] += 1

                # in Python, key cannot be list type, but tuple is ok   
                temp[tuple(char_count)] = temp.get(tuple(char_count), [])
                temp[tuple(char_count)].append(s)

            return [temp[k] for k in temp]
        
        return solution2()

        

strs = ["eat","tea","tan","ate","nat","bat"]
S = Solution()
print(S.groupAnagrams(strs))