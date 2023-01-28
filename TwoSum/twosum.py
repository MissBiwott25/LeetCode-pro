# Three Possible Solutions

# Given an array of numbers and a target number,
# return the indices of two numbers that add up to the target number

# Solutions

"""
Solution 1
O(n^2) time, O(1) space We can use two for loops to loop through the array and find the indices of the two numbers
that add up to the target number

"""

# 1. We’re looping through the list of numbers.
# 2. For each number, we’re looping through the list again, starting from the next number.
# 3. If the sum of the two numbers is equal to the target, we return the indices of the two numbers.

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

# 1. We create a dictionary called values.
# 2. We loop through the nums list.
# 3. For each number, we calculate the difference between the target and the number.
# 4. If the difference is in the values dictionary, we return the indices of the number and the difference.
# 5. If the difference is not in the values dictionary, we add the number to the dictionary.

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

# 1. We first sort the list of numbers.
# 2. We then use two pointers, one at the beginning of the list and one at the end.
# 3. We then check if the sum of the two numbers pointed by the two pointers is equal to the target.
# 4. If it is, we return the indices of the two numbers.
# 5. If it is not, we check if the sum is greater than the target. If it is, we decrement the end pointer. If it is not, we increment the start pointer.
# 6. We repeat this process until we find the two numbers whose sum is equal to the target.

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
