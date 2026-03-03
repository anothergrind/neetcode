# Given an array of integers (nums) and an integer (target)
# return the indices i and j such that the sum up to the target
# and they don't equal each other
# 
# You may assume that every input has exactly one pair of indices i and j that
# satisfy the condition
#
# Return the answer with the smaller index first
#
# Example 1:
# Input: 
#   nums = [3, 4,  5, 6], target = 7
# Output: [i, j]
#
# Example 2:
# Input: 
#   nums = [4,5,6], target = 10
# Output: [0,2]
# 
# Example 3:
# Input: 
#   nums = [5,5], target = 10
# Output: [0,1]

def twoSum(self, nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]