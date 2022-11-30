"""
Step 1: Create a variable and convert the integer into a string by storing the absolute value. Strip all the leading zeros and then reverse the string.
Afterwards store the output as an integer.

Step 2: Check if the output is in the range or not.
If it is overflown return zero.

The time complexity in this solution is O(n).

"""

class Solution:
    def reverse(self, x: int) -> int:
        ostring = str(abs(x))[::-1]
        
        if int(ostring) > 2**(31):
            ostring = '0'
        elif x < 0:
            ostring = '-' + ostring
        return(int(ostring))