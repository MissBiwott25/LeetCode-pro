# Task - Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

# 1. We start with a pointer at the beginning of the string, and a max_l variable to keep track of the longest substring.
# 2. We iterate through the string, and at each iteration, we check if the current character is in the substring we’ve already seen.
# 3. If it is, we update the max_l variable if the current substring is longer than the previous max_l.
# 4. We then move the start pointer to the next character after the duplicate character.
# 5. If the current character is not in the substring we’ve already seen, we move on to the next character.
# 6. If we reach the end of the string, we update the max_l variable if the current substring is longer than the previous max_l.
# 7. We return the max_l variable.

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        max_l = 0

        for pts in range(1, len(s)):
            if(s[pts] in s[start:pts]):
                max_l = len(s[start:pts]) if (len(s[start:pts]) > max_l) else max_l
                start = s[start:pts].index(s[pts]) + 1 + start
            else:
                if(pts == len(s) - 1):
                    max_l = max([max_l, len(s[start:])])

        return max_l if(max_l != 0) else len(s)