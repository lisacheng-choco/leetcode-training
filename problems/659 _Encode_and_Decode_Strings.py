'''
- Leetcode URL: https://www.lintcode.com/problem/659/
'''

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        '''
        encode: length + #
        '''
        res = ""
        for s in strs:
            length = str(len(s))
            res += length + "#" + s
        return res


    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        '''
        first, to find the length. Then, find the sub-string
        use two pointers to determine the string of length
        '''
        res, i = [], 0
        
        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])

            res.append(str[j+1:j+1+length])
            i = j+1+length
        return res

input = ["lint","code","love","you"]
s = Solution()

encoded_str = s.encode(input)
print(encoded_str)
print(s.decode(encoded_str))
