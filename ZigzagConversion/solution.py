# Zig Zag Conversion

# One way to solve this problem is to create a list of the required sizes and then fill each cell with the letters from the input string.


# 1. Create an array of strings, one for each row.
# 2. Iterate through the string, appending characters to the appropriate row.
# 3. The current row is determined by two variables: the current row and the current direction.
# 4. The current direction changes only when we moved up to the topmost row or down to the bottommost row.

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows  < 2):
            return s
        arr = ['' for i in range(numRows)]
        direction = 'down'
        row = 0
        for i in s:
            arr[row] += i
            if row == numRows-1:
                direction = 'up'
            elif row == 0:
                direction = 'down'
            if(direction == 'down'):
                row += 1
            else:
                row -= 1
        return(''.join(arr))