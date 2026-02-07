"""
LeetCode #1: Two Sum
Difficulty: Easy
Date: 2026-01-15
Status: Solved ✓
Time: 20 minutes

Problem:
Given an array of integers nums and an integer target, return indices 
of the two numbers that add up to target.

Approach:
- Use hash map to store complements
- Single pass solution
- Time: O(n), Space: O(n)

Pattern: Hash Map, Array
"""

def twoSum(nums, target):
    seen = {}  # num -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return []

# Test cases
print(twoSum([2,7,11,15], 9))  # [0,1]
print(twoSum([3,2,4], 6))      # [1,2]