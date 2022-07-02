'''
- Leetcode URL: https://leetcode.com/problems/valid-anagram/
- Video: https://www.youtube.com/watch?v=3OamzN90kPg
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def solution1():
            '''
            use two hash tables to write down the occurence of characters in a string

            - time complexity: O(s+t)
            - space complexity: O(s+t)
            '''
            if len(s) != len(t):
                return False
            
            dict_s, dict_t = {}, {}
            for i in range(len(s)):
                dict_s[s[i]] = 1 + dict_s.get(s[i], 0)
                dict_t[t[i]] = 1 + dict_t.get(t[i], 0)

            for c in dict_s:
                if dict_s[c] != dict_t.get(c, 0):
                    return False
            
            return True
        
        def solution2():
            '''
            sorted and compare

            - time complexity: O(n^2) or O(nlogn) depend on what sort algorithm
            - space complexity: O(1)
            '''
            return sorted(s) == sorted(t)


        return solution2()
    
s = "anagram"
t = "nagaram"
S = Solution()
print(S.isAnagram(s, t))