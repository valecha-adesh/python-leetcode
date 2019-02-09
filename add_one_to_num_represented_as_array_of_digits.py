# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.

class Solution:
    def plusOne(self, digits: 'List[int]') -> 'List[int]':
        
        a = int(''.join(str(e) for e in digits))
        s_list = list(str(a + 1))
        for i in range(len(s_list)):
            s_list[i] = int(s_list[i])
        return s_list
