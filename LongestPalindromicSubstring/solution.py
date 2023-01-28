# Challenge

# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Solution

# To find palindromic substring, we need to know the start index and end index for each substring.
# The start index and end index will range the substring as outter boundary.
# If the start element and end element are same, then we check if the substring of [start index + 1:end index] is palindromic.
# If it is and the current length of substring[start:end+1] is greater than maximum substring then we update the maxmium substring.
# Note that, single character is palindromic.

# Methodology of Two Pointers

# Iterate the whole string by each character. For each character, there are two pointers.

# The left pointer: The index of previous character in terms of current character.
# The right pointer: The index of next character in terms of current character.

# Conditions

# If previous character and next character are same. We move the left pointer one index to the left and move the right pointer on
# index to the right.

# If the left pointer or right pointer out of index or previous character and next character are not equal,
# return the string that in range between left and right pointers.
# If the returned string is longer than the longest string, replace the longest string by returned string.


# Code 1 :: (Dynamic Programming)
# 1. We start from the end of the string and work our way to the beginning.
# 2. We check if the substring from start to end is a palindrome.
# 3. If it is, we check if it’s the longest palindrome we’ve seen so far.
# 4. If it is, we update the longest palindrome we’ve seen so far.
def longestPalindrome(self, s: str) -> str:
        longest = '' if not s else s[0]
        max_len = 1
        size = len(s)
        dp=[[False]*size for _ in range(size)]
        for start in range(size-1,-1,-1):
            dp[start][start]=True
            for end in range(start+1,size):
                if s[start]==s[end]:
                    if end - start == 1 or dp[start+1][end-1]:
                        dp[start][end] = True
                        if max_len < end - start + 1:
                            max_len = end - start + 1
                            longest = s[start: end+ 1]
        return longest


#Code 2 :: (Two Pointers)

# 1. We start with a function findLongest that takes in a string s, and two indices l and r.
# 2. We check if the characters at indices l and r are the same. If they are, we increment r and decrement l.
# 3. We keep doing this until we find a mismatch.
# 4. We return the substring between l and r.
# 5. We then iterate through the string s.
# 6. For each index i, we call findLongest with i as the middle index.
# 7. We also call findLongest with i and i+1 as the middle indices.
# 8. We then return the longest substring.
def longestPalindrome(self, s: str) -> str:
        longest = ''
        def findLongest(s, l, r):
            while l>=0 and r<len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return s[l+1:r]

        for i in range(len(s)):
            s1 = findLongest(s, i, i)
            if len(s1) > len(longest): longest = s1

            s2 = findLongest(s, i, i+1)
            if len(s2) > len(longest): longest = s2

        return longest


# Big O
# When iterate the whole string, the BigO is O(n) where n is size of the string.
# Each character will need at most n/2 iteration to find if the string block is palindromic. So bigO is O(n*n/2) which is O(n^2)