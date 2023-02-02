
// 1. First, we ignore any whitespace characters at the beginning of the string.
// 2. Then, we check if the first non-whitespace character is a sign character. If it is, we set the sign accordingly.
// 3. Then, we iterate through the remaining characters and update the result.
// 4. If the current character is not a digit, we break out of the loop.
// 5. If the current result is greater than Integer.MAX_VALUE/10, we know it is going to be greater than Integer.MAX_VALUE since Integer.MAX_VALUE = 2147483647.
// 6. If the current result is equal to Integer.MAX_VALUE/10, we check to see if the current digit is greater than 7. If it is, we know the result is going to be greater than Integer.MAX_VALUE.
// 7. If the current result is less than Integer.MIN_VALUE/10, we know it is going to be less than Integer.MIN_VALUE since Integer.MIN_VALUE = -2147483648.
// 8. If the current result is equal to Integer.MIN_VALUE/10, we check to see if the current digit is less than -8. If it is, we know the result is going to be less than Integer.MIN_VALUE.
// 9. Finally, we return the result.

class Solution {
    public int myAtoi(String s) {
        int result=0;    // helper variables
        int i=0;
        int sign=1;

        while(i<s.length()&&s.charAt(i)==' ')i++;  //ignore leading white space
        if(i==s.length())return 0;
        if(s.charAt(i)=='-'||s.charAt(i)=='+')          //check if number positve or negative
        {
            sign=s.charAt(i)=='-'?-1:1;
            i++;
        }
        // now iterate across digits if any
    // should only be in range 0-9
        while(i<s.length()&&(s.charAt(i)>='0'&&s.charAt(i)<='9'))  //traverse string till nondigit not found or string ends
        {
            int digit=(s.charAt(i)-'0')*sign;
            if(sign==1 && (result>Integer.MAX_VALUE/10 || (result==Integer.MAX_VALUE/10 && digit>Integer.MAX_VALUE%10))) return Integer.MAX_VALUE; //check for overflow
            if(sign==-1 &&(result<Integer.MIN_VALUE/10 || (result==Integer.MIN_VALUE/10 && digit<Integer.MIN_VALUE%10))) return Integer.MIN_VALUE; //check for underflow

            result=result*10+digit; // update result
            i++;
        }

    return result;
    }
}
