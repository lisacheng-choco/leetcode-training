from calendar import c


class Solution:
    '''
    notes:
        1. determine if a character is aplha or numeric
            - use ASCII 
            - use Python build-in function: isalnum() / isalpha(), isnumeric()
        2. how to reverse
            - for a list: l.reverse() (return None)  / reversed(l) (return list) / l[::-1]
            - for a string or tuple: reversed(s), s[::-1] / reversed(t), t[::-1]
    '''
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

        def solution3():
            '''
            reverse s to check if it's the same

            - time complexity: O(n)
            - space complexity: O(n)
            '''
            def isalphanum(c):
                '''
                use ASCII to determine if character isalpha or numeric
                '''
                return (ord("A") <= ord(c) <= ord("Z") or
                        ord("a") <= ord(c) <= ord("z") or
                        ord("0") <= ord(c) <= ord("9"))
            new_str = ""
            for c in s:
                if isalphanum(c):
                    new_str += c
            return new_str == new_str[::-1]
        
            
        return solution3()

input = "0P" #"A man, a plan, a canal: Panama"
sol = Solution()
print(sol.isPalindrome(input))
