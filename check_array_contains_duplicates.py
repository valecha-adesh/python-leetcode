# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: 'List[int]') -> 'bool':
        if len(nums) != len(set(nums)):
            return True
        else:
            return False
        
