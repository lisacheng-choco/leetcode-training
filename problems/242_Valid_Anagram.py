'''
- Leetcode URL: https://leetcode.com/problems/valid-anagram/
- Video: https://www.youtube.com/watch?v=3OamzN90kPg
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def solution1():
            '''
            use two hash tables to write down the occurence of characters in a string

            - time complexity: O(n)
            - space complexity: O(n)
            '''
            dict_s = {}
            dict_t = {}
            for i in range(len(s)):
                if dict_s.get(s[i]) is None:
                    dict_s[s[i]] = 1
                else:
                    dict_s[s[i]] = dict_s[s[i]] + 1

            for i in range(len(t)): 
                if dict_t.get(t[i]) is None:
                    dict_t[t[i]] = 1
                else:
                    dict_t[t[i]] = dict_t[t[i]] + 1

            if dict_s == dict_t:
                return True
            else:
                return False

        return solution1()
    
s = "anagram"
t = "nagaram"
S = Solution()
print(S.isAnagram(s, t))