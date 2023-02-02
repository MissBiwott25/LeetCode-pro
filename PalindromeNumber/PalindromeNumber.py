# 1. First, we check if the number is negative. If it is, then we return False.
# 2. Then, we reverse the number.
# 3. Finally, we compare the reversed number with the original number. If they are equal, then we return True. Otherwise, we return False.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        rev = 0
        while x > 0:
            dig = (x % 10)
            rev = (rev * 10) + dig
            x = x // 10
        if (temp == rev):
            return True
        else:
            return False

# Since we are going through the entire number digit by digit, the time complexity should be O(log10n).
# Because we are dividing the number by 10 in every iteration. So the time complexity can be said is equal to the number of digits in a number.

# Space Complexity : O(1) because we are using one extra variable to store the reversed number.
