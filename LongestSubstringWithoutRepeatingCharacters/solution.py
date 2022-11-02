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