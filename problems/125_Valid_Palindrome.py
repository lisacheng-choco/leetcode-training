class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        create 2 pointers: fore & back
        iterate the 's', fore begins at the first position and back begins at the last position
            if back and fore point to the same position, return true
            else check if the same character
        
        - time complexity: O(n)
        - space complexity: O(1)
        '''

        def solution1():
            
            start, end = 0, len(s)-1
            while start < end:
                if not s[start].isalpha() and not s[start].isnumeric():
                    start +=1
                    continue
                if not s[end].isalpha() and not s[end].isnumeric():
                    end -=1
                    continue
                if s[start].lower() != s[end].lower():
                    return False
                start += 1
                end -= 1
                
            return True
        return solution1()

input = "0P" #"A man, a plan, a canal: Panama"
sol = Solution()
print(sol.isPalindrome(input))
