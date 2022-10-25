# Three Possible Solutions

# Given an array of numbers and a target number, 
# return the indices of two numbers that add up to the target number

# Solutions

"""
Solution 1
O(n^2) time, O(1) space We can use two for loops to loop through the array and find the indices of the two numbers 
that add up to the target number
    
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

"""
Solution 2
O(n) time, O(n) space We can use a hash table to store the numbers as keys and the indices as values. 
Then we check to see if the difference (target - number) is in the hash table.
If it is, return both the index of the number and the index of the difference
    
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in values:
                return [i, values[diff]]
            values[num] = i
        return []
    
"""
Solution 3
O(nlogn) time, O(1) space You can use the two pointer method.
After sorting the array and creating an array of the numbers and their indices, 
create two pointers i and j where i = 0 and j = len(array)-1. 
If the sum is smaller than target, increment i, if larger, increment j. 
If equal, return the indices.
    
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        sortedNums = sorted(zip(nums, range(len(nums))))
        while i < j:
            if sortedNums[i][0] + sortedNums[j][0] == target:
                return [sortedNums[i][1], sortedNums[j][1]]
            elif sortedNums[i][0] + sortedNums[j][0] < target:
                i += 1
            elif sortedNums[i][0] + sortedNums[j][0] > target:
                j -= 1
