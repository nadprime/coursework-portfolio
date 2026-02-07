# Two Sum

**Date:** 2026-01-15  
**Difficulty:** Easy  
**Status:** ✓ Solved  
**Time Taken:** 20 minutes  

## Problem
[Link to LeetCode](https://leetcode.com/problems/two-sum/)

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

## Initial Thoughts
- Brute force: Check every pair → O(n²)
- Need something faster
- Hash map might help

## Approach 1: Brute Force (Not Implemented)
- Nested loops
- Time: O(n²), Space: O(1)
- Too slow for large inputs

## Approach 2: Hash Map (Implemented) ✓
- Store each number and its index in hash map
- For each number, check if complement exists
- Time: O(n), Space: O(n)

## Code
See `two-sum.py`

## Mistakes Made
- Initially forgot to check if complement exists before accessing
- Edge case: What if array has duplicates? (Handled by checking index)

## Lessons Learned
- Hash map pattern perfect for "find complement" problems
- Always think about one-pass solutions
- Consider: Can I trade space for time?

## Similar Problems
- Three Sum (LeetCode #15)
- Two Sum II (LeetCode #167)

## Pattern Identified
**Hash Map for Complements**: When looking for pairs that sum to target, use hash map to store seen elements. This allows for O(1) lookups and enables a one-pass solution.